let isStreaming = false;
let allChannels = [];
let presets = [];
let hwinfoAvailable = false;
let groupsCollapsed = false;
let pollInterval = null;

// Above this, session start gets slow: ATLAS registers each parameter with its
// own gRPC round-trip, so a few hundred channels is a real wait.
const CHANNEL_WARNING_THRESHOLD = 250;

document.addEventListener('DOMContentLoaded', async () => {
    await refreshChannels();
    document.getElementById('preset').addEventListener('change', onPresetChange);
    document.getElementById('channel-search').addEventListener('input', applyChannelFilter);
    startPolling();
});

// --- Data Loading ---

async function refreshChannels() {
    try {
        const resp = await fetch('/api/channels');
        const data = await resp.json();

        hwinfoAvailable = data.available;
        allChannels = data.channels || [];
        presets = data.presets || [];

        const notice = document.getElementById('hwinfo-notice');
        if (!hwinfoAvailable) {
            document.getElementById('hwinfo-error').textContent = data.error || '';
            notice.style.display = 'block';
        } else {
            notice.style.display = 'none';
        }

        buildPresetOptions();
        buildChannelPicker();
        onPresetChange();
        applyAvailability();
    } catch (e) {
        showError('Failed to load channels: ' + e.message);
    }
}

function applyAvailability() {
    if (isStreaming) return;

    const btn = document.getElementById('btn-toggle');
    if (hwinfoAvailable) {
        btn.disabled = false;
        btn.textContent = 'Start Streaming';
        return;
    }

    // Nothing to stream and nothing to pick from until HWiNFO is publishing.
    btn.disabled = true;
    btn.textContent = 'HWiNFO unavailable';
    document.getElementById('channel-picker').style.display = 'none';
    document.getElementById('preset-hint').textContent =
        'Enable HWiNFO shared memory above, then press Retry.';
}

function buildPresetOptions() {
    const select = document.getElementById('preset');
    const previous = select.value;
    select.innerHTML = '';

    for (const preset of presets) {
        const opt = document.createElement('option');
        opt.value = preset.name;
        opt.textContent = `${titleCase(preset.name)} (${preset.channel_count})`;
        opt.dataset.description = preset.description;
        opt.dataset.count = preset.channel_count;
        select.appendChild(opt);
    }

    const custom = document.createElement('option');
    custom.value = 'custom';
    custom.textContent = 'Custom...';
    custom.dataset.description = 'Pick individual readings below';
    custom.dataset.count = '0';
    select.appendChild(custom);

    if (previous) select.value = previous;
    if (!select.value) select.value = 'essential';
}

function titleCase(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
}

// --- Channel Picker ---

function buildChannelPicker() {
    const container = document.getElementById('channel-groups');
    container.innerHTML = '';

    const groups = new Map();
    for (const ch of allChannels) {
        if (!groups.has(ch.group)) groups.set(ch.group, []);
        groups.get(ch.group).push(ch);
    }

    for (const [groupName, channels] of groups) {
        const groupDiv = document.createElement('div');
        groupDiv.className = 'channel-group';
        groupDiv.dataset.group = groupName;

        const title = document.createElement('div');
        title.className = 'channel-group-title';

        const caret = document.createElement('span');
        caret.className = 'group-caret';
        caret.textContent = '▾';

        const name = document.createElement('span');
        name.className = 'group-name';
        name.textContent = groupName;

        const count = document.createElement('span');
        count.className = 'group-count';
        count.textContent = `${channels.length}`;

        const all = document.createElement('button');
        all.type = 'button';
        all.className = 'group-select';
        all.textContent = 'all';
        all.onclick = (e) => {
            e.stopPropagation();
            setGroupChecked(groupDiv, true);
        };

        const none = document.createElement('button');
        none.type = 'button';
        none.className = 'group-select';
        none.textContent = 'none';
        none.onclick = (e) => {
            e.stopPropagation();
            setGroupChecked(groupDiv, false);
        };

        title.append(caret, name, count, all, none);
        title.onclick = () => groupDiv.classList.toggle('collapsed');
        groupDiv.appendChild(title);

        const items = document.createElement('div');
        items.className = 'channel-group-items';

        for (const ch of channels) {
            const wrapper = document.createElement('label');
            wrapper.className = 'channel-checkbox';
            wrapper.title = `${ch.metric_key}\n${ch.description}`;
            wrapper.dataset.search = `${ch.group} ${ch.label} ${ch.units} ${ch.reading_type}`.toLowerCase();

            const cb = document.createElement('input');
            cb.type = 'checkbox';
            cb.value = ch.metric_key;
            cb.onchange = updateSelectedCount;

            const text = document.createElement('span');
            text.className = 'channel-label';
            text.textContent = ch.label;

            const value = document.createElement('span');
            value.className = 'channel-value';
            value.textContent = ch.value === null || ch.value === undefined
                ? '--'
                : `${formatNumber(ch.value)}${ch.units ? ' ' + ch.units : ''}`;

            wrapper.append(cb, text, value);
            items.appendChild(wrapper);
        }

        groupDiv.appendChild(items);
        container.appendChild(groupDiv);
    }

    updateSelectedCount();
}

function setGroupChecked(groupDiv, checked) {
    groupDiv.querySelectorAll('.channel-checkbox').forEach(item => {
        if (item.style.display !== 'none') item.querySelector('input').checked = checked;
    });
    updateSelectedCount();
}

function applyChannelFilter() {
    const query = document.getElementById('channel-search').value.trim().toLowerCase();

    document.querySelectorAll('.channel-group').forEach(groupDiv => {
        let visible = 0;
        groupDiv.querySelectorAll('.channel-checkbox').forEach(item => {
            const match = !query || item.dataset.search.includes(query);
            item.style.display = match ? '' : 'none';
            if (match) visible++;
        });
        groupDiv.style.display = visible ? '' : 'none';
        // A filtered search is useless behind a collapsed header.
        if (query) groupDiv.classList.remove('collapsed');
    });
}

function toggleAllGroups() {
    groupsCollapsed = !groupsCollapsed;
    document.querySelectorAll('.channel-group').forEach(g => {
        g.classList.toggle('collapsed', groupsCollapsed);
    });
}

function selectAllChannels() {
    document.querySelectorAll('#channel-groups input[type="checkbox"]').forEach(cb => cb.checked = true);
    updateSelectedCount();
}

function deselectAllChannels() {
    document.querySelectorAll('#channel-groups input[type="checkbox"]').forEach(cb => cb.checked = false);
    updateSelectedCount();
}

function selectVisibleChannels() {
    document.querySelectorAll('.channel-checkbox').forEach(item => {
        if (item.style.display !== 'none') item.querySelector('input').checked = true;
    });
    updateSelectedCount();
}

function getSelectedCustomChannels() {
    return Array.from(
        document.querySelectorAll('#channel-groups input[type="checkbox"]:checked')
    ).map(cb => cb.value);
}

function updateSelectedCount() {
    const count = getSelectedCustomChannels().length;
    document.getElementById('picker-count').textContent = `${count} selected`;
    showChannelWarning(count);
}

function showChannelWarning(count) {
    const warning = document.getElementById('picker-warning');
    if (count > CHANNEL_WARNING_THRESHOLD) {
        warning.textContent =
            `${count} channels selected. ATLAS registers every parameter individually, ` +
            `so starting a session with this many will take a while.`;
        warning.style.display = 'block';
    } else {
        warning.style.display = 'none';
    }
}

function onPresetChange() {
    const select = document.getElementById('preset');
    const option = select.selectedOptions[0];
    const isCustom = select.value === 'custom';

    document.getElementById('channel-picker').style.display = isCustom ? 'block' : 'none';
    document.getElementById('preset-hint').textContent = option ? option.dataset.description : '';

    if (isCustom) {
        updateSelectedCount();
    } else {
        showChannelWarning(option ? Number(option.dataset.count) : 0);
    }
}

// --- Bridge Control ---

async function toggleBridge() {
    if (isStreaming) {
        await stopBridge();
    } else {
        await startBridge();
    }
}

async function startBridge() {
    const btn = document.getElementById('btn-toggle');
    btn.disabled = true;
    btn.textContent = 'Starting...';

    const preset = document.getElementById('preset').value;
    const body = { session_name: document.getElementById('session-name').value || null };

    if (preset === 'custom') {
        body.preset = null;
        body.custom_channels = getSelectedCustomChannels();
        if (body.custom_channels.length === 0) {
            showError('No channels selected');
            resetStartButton();
            return;
        }
    } else {
        body.preset = preset;
    }

    try {
        const resp = await fetch('/api/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body),
        });
        const data = await resp.json();

        if (data.success) {
            isStreaming = true;
            updateUIForStreaming();
        } else {
            showError(data.error || data.message || 'Failed to start');
            resetStartButton();
        }
    } catch (e) {
        showError('Connection error: ' + e.message);
        resetStartButton();
    }
}

function resetStartButton() {
    const btn = document.getElementById('btn-toggle');
    btn.disabled = false;
    btn.textContent = 'Start Streaming';
}

async function stopBridge() {
    const btn = document.getElementById('btn-toggle');
    btn.disabled = true;
    btn.textContent = 'Stopping...';

    try {
        await fetch('/api/stop', { method: 'POST' });
        isStreaming = false;
        updateUIForStopped();
    } catch (e) {
        showError('Failed to stop: ' + e.message);
    }

    btn.disabled = false;
}

// --- Status Polling ---

function startPolling() {
    pollInterval = setInterval(pollStatus, 500);
}

async function pollStatus() {
    try {
        const resp = await fetch('/api/status');
        updateStatusDisplay(await resp.json());
    } catch {
        // Server unreachable, ignore
    }
}

function updateStatusDisplay(status) {
    const sourceUp = status.streaming_active ? status.source_connected : hwinfoAvailable;
    setDot('dot-source', sourceUp, status.streaming_active && !status.source_connected);
    setDot('dot-atlas', status.atlas_connected, false);
    setDot('dot-streaming', status.streaming_active, false);

    document.getElementById('status-source').textContent =
        sourceUp ? 'Connected' : status.streaming_active ? 'Waiting...' : 'Not available';

    document.getElementById('status-atlas').textContent =
        status.atlas_connected ? 'Connected' : 'Disconnected';

    document.getElementById('status-streaming').textContent =
        status.streaming_active ? 'Active' : 'Stopped';

    document.getElementById('stat-channels').textContent =
        `${status.channel_count || 0} channels`;
    document.getElementById('stat-samples').textContent =
        `${status.samples_sent.toLocaleString()} samples`;

    const elapsed = Math.floor(status.elapsed_seconds);
    document.getElementById('stat-elapsed').textContent =
        `${Math.floor(elapsed / 60)}:${(elapsed % 60).toString().padStart(2, '0')}`;

    if (status.streaming_active && !isStreaming) {
        isStreaming = true;
        updateUIForStreaming();
    } else if (!status.streaming_active && isStreaming) {
        isStreaming = false;
        updateUIForStopped();
    }

    if (status.error) showError(status.error);

    // A poll age that keeps climbing means HWiNFO has stopped publishing —
    // usually the free version's 12-hour shared-memory timeout.
    if (status.streaming_active && status.hwinfo_poll_age_seconds > 30) {
        showError(
            `HWiNFO has not refreshed its shared memory for ` +
            `${Math.round(status.hwinfo_poll_age_seconds)}s. Values may be stale — ` +
            `restart HWiNFO if this persists.`
        );
    }

    if (status.streaming_active && Object.keys(status.current_values).length > 0) {
        updateTelemetryTable(status.current_values, status.active_channels);
    }

    if (status.streaming_active && status.insights && status.insights.length > 0) {
        updateAnalysisList(status.insights);
    }
}

function setDot(id, connected, waiting) {
    const dot = document.getElementById(id);
    dot.className = 'status-dot';
    if (connected) dot.classList.add('connected');
    else if (waiting) dot.classList.add('waiting');
}

// --- Analysis ---

function updateAnalysisList(insights) {
    document.getElementById('analysis-section').style.display = 'block';
    document.getElementById('analysis-list').innerHTML = insights
        .map(i => `<div class="insight-item ${i.level}">${escapeHtml(i.message)}</div>`)
        .join('');
}

// --- Telemetry Table ---

function updateTelemetryTable(values, activeChannels) {
    document.getElementById('telemetry-section').style.display = 'block';

    const byKey = new Map(allChannels.map(c => [c.metric_key, c]));
    const groups = new Map();
    for (const key of activeChannels) {
        const ch = byKey.get(key);
        const group = ch ? ch.group : 'Other';
        if (!groups.has(group)) groups.set(group, []);
        groups.get(group).push({ key, ch });
    }

    let html = '';
    for (const [groupName, items] of groups) {
        html += `<div class="telem-group"><div class="telem-group-title">${escapeHtml(groupName)}</div><div class="telem-grid">`;
        for (const { key, ch } of items) {
            const val = values[key];
            const display = val === undefined ? '--' : formatNumber(val);
            const units = ch && ch.units ? ch.units : '';
            const name = ch ? ch.label : key;
            html += `<div class="telem-item" title="${escapeHtml(key)}">`;
            html += `<span class="telem-name">${escapeHtml(name)}</span>`;
            html += `<span class="telem-value">${display}<span class="telem-units"> ${escapeHtml(units)}</span></span>`;
            html += `</div>`;
        }
        html += `</div></div>`;
    }

    document.getElementById('telemetry-table').innerHTML = html;
}

function formatNumber(val) {
    if (val === null || val === undefined) return '--';
    const abs = Math.abs(val);
    if (abs >= 10000) return val.toFixed(0);
    if (abs >= 100) return val.toFixed(1);
    if (abs >= 1) return val.toFixed(2);
    if (abs === 0) return '0';
    return val.toFixed(3);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text == null ? '' : String(text);
    return div.innerHTML;
}

// --- UI State ---

function updateUIForStreaming() {
    const btn = document.getElementById('btn-toggle');
    btn.textContent = 'Stop Streaming';
    btn.className = 'btn-start running';
    btn.disabled = false;

    const config = document.getElementById('config-section');
    config.style.opacity = '0.5';
    config.style.pointerEvents = 'none';
}

function updateUIForStopped() {
    const btn = document.getElementById('btn-toggle');
    btn.textContent = 'Start Streaming';
    btn.className = 'btn-start';
    btn.disabled = false;

    const config = document.getElementById('config-section');
    config.style.opacity = '1';
    config.style.pointerEvents = 'auto';
    document.getElementById('telemetry-section').style.display = 'none';
    document.getElementById('analysis-section').style.display = 'none';
    applyAvailability();
}

// --- Error Handling ---

function showError(msg) {
    document.getElementById('error-text').textContent = msg;
    document.getElementById('error-banner').style.display = 'flex';
}

function dismissError() {
    document.getElementById('error-banner').style.display = 'none';
}
