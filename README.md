<h1 align="center">Endpoint Software Monitoring Tool</h1>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com/?lines=Endpoint+Security+Monitoring+Tool;Real-Time+Process+Detection;Network+Connection+Tracking;Cybersecurity+Python+Project&center=true&width=800&height=45&color=00ff88">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Platform-Linux-success?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Security-Endpoint%20Monitoring-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

<p align="center">
<img src="https://komarev.com/ghpvc/?username=rahatsahriarrafi&label=Project+Views&color=0e75b6&style=flat">
</p>

<hr>

<div style="background:#0d1117;color:white;padding:20px;border-radius:10px">

<h2>📌 Project Overview</h2>

<p>
The <b>Endpoint Software Monitoring Tool</b> is a lightweight Python-based cybersecurity project
designed to monitor system activity in real time.
</p>

<p>
It scans running processes, tracks network connections, and alerts users when unknown
or blacklisted software is detected.
</p>

<p>
This project demonstrates the core concepts behind <b>endpoint monitoring systems and
security monitoring tools</b>.
</p>

</div>

<hr>

<h2 align="center">⚙ Features</h2>

<ul>
<li>Real-time process monitoring</li>
<li>Network connection tracking</li>
<li>Whitelist / blacklist security policy</li>
<li>Real-time terminal alerts</li>
<li>Security event logging</li>
<li>Modular cybersecurity architecture</li>
<li>Continuous monitoring loop</li>
</ul>

<hr>

<h2 align="center">🖥 Live Monitoring Example</h2>

<div style="background:black;color:#00ff88;padding:20px;border-radius:10px;font-family:monospace">

▶ Starting Endpoint Monitor... <br>
▶ Scanning system processes... <br>
▶ Monitoring network activity... <br><br>

⚠ WARNING <br>
Unknown software detected: pipewire (PID 1365) <br><br>

[23:44:26] INFO → brave → 104.18.43.204:443 <br>
[23:44:26] INFO → code → 23.206.173.104:443 <br>

▶ System monitoring active...

</div>

<hr>

<h2 align="center">🎥 Tool Demo</h2>

<p align="center">
<img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="700">
</p>

<hr>

<h2 align="center">📂 Project Structure</h2>

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

<h2 align="center">📦 Module Description</h2>

<h3>monitor.py</h3>

<p>
Main controller that starts the monitoring loop and coordinates system scanning.
</p>

<h3>scanner.py</h3>

<p>
Collects system information including:
</p>

<ul>
<li>Running processes</li>
<li>Running services</li>
<li>Network connections per process</li>
</ul>

<h3>policy_manager.py</h3>

<p>
Handles whitelist and blacklist policies for detected processes.
</p>

<h3>notifier.py</h3>

<p>
Responsible for real-time alerts and logging system events.
</p>

<h3>config.py</h3>

<p>
Stores configuration settings such as scan interval and log paths.
</p>

<hr>

<h2 align="center">📜 Log Example</h2>

<div style="background:#f6f8fa;padding:15px;border-radius:8px;font-family:monospace">

[2026-03-11 01:21:53] WARNING: Unknown software detected: pipewire (PID 1365)

</div>

<hr>

<h2 align="center">🚀 How to Run</h2>

<div style="background:#f6f8fa;padding:15px;border-radius:8px;font-family:monospace">

pip install psutil<br><br>

cd endpoint-software-monitoring-tool<br>
python monitor.py

</div>

<hr>

<h2 align="center">📚 Educational Purpose</h2>

<p>
This project demonstrates cybersecurity monitoring concepts such as:
</p>

<ul>
<li>Endpoint monitoring</li>
<li>Process inspection</li>
<li>Network connection analysis</li>
<li>Security policy enforcement</li>
<li>Real-time event logging</li>
</ul>

<hr>

<h2 align="center">🔮 Future Improvements</h2>

<ul>
<li>IP geolocation lookup</li>
<li>Suspicious tool detection (nmap, hydra, netcat)</li>
<li>Email alerts</li>
<li>Telegram notifications</li>
<li>Web dashboard</li>
<li>Advanced SOC-style terminal UI</li>
</ul>



<hr>

<h2 align="center">👨‍💻 Authors & Contributors</h2>

<div style="background:#f6f8fa;padding:20px;border-radius:10px">

<h3>Rahat Sahriar Rafi</h3>

<ul>
<li>Project Creator</li>
<li>Designed the system architecture</li>
<li>Implemented core modules (scanner, monitor, policy manager)</li>
<li>Developed real-time process and network monitoring logic</li>
<li>Project documentation and repository management</li>
</ul>

<h3>Md. Munkasir Haque</h3>

<ul>
<li>Contributor</li>
<li>Worked on notification system improvements</li>
<li>Improved configuration security and credential handling</li>
<li>Assisted with debugging and runtime error fixes</li>
<li>Contributed to overall tool workflow enhancement</li>
</ul>

</div>

<hr>
