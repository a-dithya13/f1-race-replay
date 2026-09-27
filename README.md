# F1 Race Replay 🏎️ 🏁

An interactive Formula 1 race visualization and telemetry analysis application built with Python. It uses real F1 session data to reconstruct race events, render driver positions on track, and provide interactive replay and telemetry tools.

> **Note:** This repository is a fork of [IAmTomShaw/f1-race-replay](https://github.com/IAmTomShaw/f1-race-replay). My work on this fork focuses on extending the replay experience with driver statistics and an interactive driver information interface.

![Race Replay Preview](./resources/preview.png)

## ✨ Features

* **Race Replay Visualization** — Watch races unfold with driver positions rendered on the circuit.
* **Interactive Leaderboard** — View driver positions, tyre compounds, and race status.
* **Driver Statistics** — Select a driver from the leaderboard and view additional driver information.
* **Driver Information Popup** — Interactive popup interface for displaying driver statistics and metadata.
* **OpenF1 Integration** — Retrieves driver information using the OpenF1 API.
* **Telemetry Visualization** — Access race telemetry and analysis tools.
* **Safety Car Visualization** — Visualizes Safety Car deployment, movement, and return phases.
* **Qualifying Replay Support** — Replay qualifying sessions with telemetry visualization.
* **Interactive Playback** — Pause, rewind, fast-forward, restart, and change playback speed.
* **GUI & CLI Modes** — Select race sessions through the graphical interface or command line.
* **Telemetry Insights** — Access additional telemetry analysis through the Insights interface.

---

## 👨‍💻 My Contributions

My main contribution to this fork was extending the race replay with a **driver statistics and information system**.

### Driver Statistics System

I added a dedicated driver statistics layer that retrieves and organizes driver information from OpenF1.

Key additions include:

* `src/driver_stats.py`

  * Driver information retrieval.
  * OpenF1 API integration.
  * Session-aware driver lookup.
  * Basic caching of retrieved driver data.
  * A reusable `get_complete_driver_info()` interface.

* `src/driver_stats_data.py`

  * Driver-related data used by the statistics interface.

### Interactive Driver Popup

I created `src/driver_popup.py`, which provides a dedicated UI for displaying driver information.

The popup is integrated with the race leaderboard so that selecting a driver can open their corresponding information panel.

### Replay Interface Integration

I modified:

`src/interfaces/race_replay.py`

to connect the leaderboard interaction with the driver statistics system.

The replay interface now:

1. Detects a selected driver.
2. Requests the corresponding driver information.
3. Opens the driver statistics popup.
4. Handles popup interaction and closing.
5. Prevents underlying replay controls from receiving clicks while the popup is active.

### API Testing

I also added:

`test_openf1_api.py`

to test the OpenF1 driver-data integration independently from the main replay interface.

---

## 🖥️ Interface

### Main Replay

![Race Replay Preview](./resources/preview.png)

The main replay renders driver positions, race progress, track information, and the interactive leaderboard.

### GUI Menu

![GUI Menu Preview](./resources/gui-menu.png)

The GUI allows users to select the race session they want to replay.

### CLI Menu

![CLI Menu Preview](./resources/cli-menu.gif)

The project also supports a command-line session selection workflow.

> A driver statistics popup screenshot can be added here once the final UI version is captured.

---

## 🎮 Controls

| Action                  | Control                 |
| ----------------------- | ----------------------- |
| Pause / Resume          | `SPACE`                 |
| Rewind                  | `←`                     |
| Fast Forward            | `→`                     |
| Increase Playback Speed | `↑`                     |
| Decrease Playback Speed | `↓`                     |
| Set Speed Directly      | `1`–`4`                 |
| Restart Replay          | `R`                     |
| Toggle DRS Zone         | `D`                     |
| Toggle Progress Bar     | `B`                     |
| Toggle Driver Names     | `L`                     |
| Select Driver           | Click leaderboard entry |
| Select Multiple Drivers | Shift + Click           |

---

## 🏎️ Safety Car Visualization

The replay includes a simulated Safety Car whenever the underlying F1 data indicates a Safety Car deployment.

Because the available F1 telemetry does not provide GPS telemetry for the actual Safety Car, its position is estimated relative to the race leader.

The visualization includes:

* Deployment animation
* On-track state
* Return-to-pit animation
* Visual status indicators
* Position interpolation along the circuit

---

## 📊 Driver Statistics

The driver statistics feature extends the existing leaderboard interaction.

When a driver is selected, the application can retrieve additional information through OpenF1 and present it in a dedicated popup.

The system is designed around:

```text
Race Leaderboard
       │
       ▼
Selected Driver
       │
       ▼
get_complete_driver_info()
       │
       ▼
OpenF1 / Cached Data
       │
       ▼
DriverPopup
```

This keeps the data-retrieval logic separate from the UI layer and makes the driver information functionality reusable.

---

## 📡 Telemetry & Insights

The project includes an Insights system for accessing telemetry analysis tools while a replay is running.

The telemetry system can expose information such as:

* Speed
* Gear
* DRS
* Lap information
* Driver telemetry
* Track position
* Lap-time evolution
* Tyre strategy
* Race control information

Additional documentation can be found in:

* `docs/InsightsMenu.md`
* `docs/PitWallWindow.md`
* `docs/Testing.md`
* `telemetry.md`

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **Arcade** — graphical rendering and UI
* **FastF1** — Formula 1 session and telemetry data
* **NumPy** — numerical processing
* **SciPy** — spatial calculations
* **OpenF1 API** — driver information
* **Pytest** — automated testing

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/a-dithya13/f1-race-replay.git
cd f1-race-replay
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

For development and testing:

```bash
pip install -r requirements-dev.txt
```

### 4. Run the application

```bash
python main.py
```

This launches the GUI session selector.

### CLI mode

```bash
python main.py --cli
```

### Run a specific race

```bash
python main.py --viewer --year 2025 --round 12
```

### Run without HUD

```bash
python main.py --viewer --year 2025 --round 12 --no-hud
```

### Run a Sprint session

```bash
python main.py --viewer --year 2025 --round 12 --sprint
```

### Run a Qualifying session

```bash
python main.py --viewer --year 2025 --round 12 --qualifying
```

### Refresh telemetry data

```bash
python main.py --viewer --year 2025 --round 12 --refresh-data
```

---

## 🧪 Testing

The repository uses `pytest` for automated testing.

Run the test suite with:

```bash
python -m pytest
```

The current project test suite contains tests covering settings, seasons, time utilities, tyres, and imports.

The driver statistics work also includes:

```bash
python test_openf1_api.py
```

for testing the OpenF1 integration separately.

---

## 📁 Project Structure

```text
f1-race-replay/
│
├── main.py
├── README.md
├── requirements.txt
├── requirements-dev.txt
│
├── docs/
│   ├── InsightsMenu.md
│   ├── PitWallWindow.md
│   └── Testing.md
│
├── resources/
│   ├── preview.png
│   ├── gui-menu.png
│   └── cli-menu.gif
│
├── src/
│   ├── f1_data.py
│   ├── ui_components.py
│   ├── run_session.py
│   │
│   ├── driver_popup.py
│   ├── driver_stats.py
│   ├── driver_stats_data.py
│   │
│   ├── interfaces/
│   │   └── race_replay.py
│   │
│   ├── insights/
│   ├── gui/
│   ├── services/
│   └── lib/
│
├── tests/
│
└── test_openf1_api.py
```

---

## 🔧 Troubleshooting

If FastF1 data loading fails, try:

```bash
pip install --upgrade fastf1
```

The first time a session is loaded, telemetry data may take longer to download and process. Subsequent runs can use cached data.

If you encounter an OpenGL-related error with Arcade, check that your graphics environment supports the required OpenGL version.

---

## 🤝 About This Fork

This repository builds on the original F1 Race Replay project and adds functionality focused on making individual driver data more accessible during a replay.

The main extension is the driver statistics workflow:

**Leaderboard → Driver Selection → Driver Data → Interactive Popup**

The goal is to make the replay more than a visual playback tool by connecting race visualization with driver-level information.

---

## 📜 License

This project follows the MIT License of the original project.

Formula 1 and related trademarks belong to their respective owners. This project is intended for educational and non-commercial use.

---

## 🙌 Acknowledgements

Original project:

[IAmTomShaw/f1-race-replay](https://github.com/IAmTomShaw/f1-race-replay)

Built using:

* FastF1
* Arcade
* NumPy
* SciPy
* OpenF1
* Pytest
