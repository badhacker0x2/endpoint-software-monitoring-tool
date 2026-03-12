<h1 align="center">Endpoint Software Monitoring Tool</h1>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com/?lines=Endpoint+Security+Monitor;Real-time+Process+Detection;Network+Connection+Tracking;Cybersecurity+Learning+Project&center=true&width=700&height=45">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue">
<img src="https://img.shields.io/badge/Platform-Linux-green">
<img src="https://img.shields.io/badge/Security-Endpoint%20Monitoring-orange">
<img src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

<hr>

<div style="background:#0d1117;color:white;padding:20px;border-radius:10px">

<h2>📌 Project Overview</h2>

<p>
The <b>Endpoint Software Monitoring Tool</b> is a lightweight Python-based cybersecurity project
designed to monitor system activity in real time.
</p>

<p>
It scans running processes, tracks network connections, and alerts the user when unknown
or blacklisted software is detected.
</p>

<p>
This project demonstrates the core concepts behind <b>endpoint monitoring systems and
security monitoring tools</b>.
</p>

</div>

<hr>

<h2>⚙ Features</h2>

<ul>
<li>Real-time process monitoring</li>
<li>Network connection tracking</li>
<li>Whitelist / blacklist policy management</li>
<li>Security alert system</li>
<li>Real-time terminal monitoring</li>
<li>Event logging</li>
<li>Modular architecture</li>
</ul>

<hr>

<h2>🖥 Live Monitoring Example</h2>

<div style="background:black;color:#00ff88;padding:15px;border-radius:6px;font-family:monospace">

===== Endpoint Software Monitoring Tool ===== <br>
Real-time monitoring started... <br><br>

⚠ WARNING <br>
Unknown software detected: pipewire (PID 1365) <br><br>

[23:44:26] INFO → brave → 104.18.43.204:443 <br>
[23:44:26] INFO → code → 23.206.173.104:443 <br>

</div>

<hr>

<h2>📂 Project Structure</h2>

<div style="background:#f6f8fa;padding:15px;border-radius:8px;font-family:monospace">

endpoint-software-monitoring-tool<br>
│<br>
├── monitor.py<br>
├── scanner.py<br>
├── policy_manager.py<br>
├── notifier.py<br>
├── config.py<br>
│<br>
├── data<br>
│   ├── whitelist.txt<br>
│   └── blacklist.txt<br>
│<br>
├── logs<br>
│   └── monitor.log<br>
│<br>
└── README.md

</div>

<hr>

<h2>📦 Module Description</h2>

<h3>monitor.py</h3>

<p>
Main controller responsible for running the monitoring loop and coordinating system scans.
</p>

<h3>scanner.py</h3>

<p>
Collects system information including running processes, services, and active network connections.
</p>

<h3>policy_manager.py</h3>

<p>
Handles whitelist and blacklist policies for detected processes.
</p>

<h3>notifier.py</h3>

<p>
Displays alerts and logs security events.
</p>

<h3>config.py</h3>

<p>
Stores configuration values such as scan interval and log file paths.
</p>

<hr>

<h2>📜 Log Example</h2>

<div style="background:#f6f8fa;padding:15px;border-radius:8px;font-family:monospace">

[2026-03-11 01:21:53] WARNING: Unknown software detected: pipewire (PID 1365)

</div>

<hr>

<h2>🚀 How to Run</h2>

<div style="background:#f6f8fa;padding:15px;border-radius:8px;font-family:monospace">

pip install psutil<br><br>

cd endpoint-software-monitoring-tool<br>
python monitor.py

</div>

<hr>

<h2>📚 Educational Purpose</h2>

<p>
This project demonstrates important cybersecurity monitoring concepts such as:
</p>

<ul>
<li>Endpoint monitoring</li>
<li>Process inspection</li>
<li>Network connection analysis</li>
<li>Security policy enforcement</li>
<li>Real-time event logging</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>IP geolocation lookup</li>
<li>Suspicious tool detection (nmap, hydra, netcat)</li>
<li>Email alerts</li>
<li>Telegram notifications</li>
<li>Web dashboard</li>
<li>Live SOC-style terminal UI</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Rahat Sahriar Rafi</b><br>
Cybersecurity & Python Learning Project
</p>
