# Dota Stats Analysis

This project focuses on analyzing Dota 2 match data, aiming to extract insights from player and team performance metrics. The analysis includes data preparation, feature engineering, exploratory data analysis (EDA), and predictive modeling to understand game dynamics better and highlight potential strategies.

## Table of Contents

- [Overview](#overview)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Analysis](#analysis)
- [Contributing](#contributing)
- [License](#license)

## Overview

Dota 2 is a popular multiplayer online battle arena (MOBA) game that provides rich data on matches, players, and game events. This project collects, preprocesses, and analyzes Dota 2 match data to study trends in gameplay, performance metrics, and team strategies.

## Data

The dataset used in this project includes match statistics, objectives, player roles, and more. It can be fetched using the [OpenDota API](https://docs.opendota.com/), and this project focuses on using the following main data attributes:

- **Match ID**: Unique identifier for each match
- **Hero Stats**: Attributes for each hero, including primary attributes, attack type, and role
- **Objectives**: Events in the match, such as first blood, tower kills, and barracks status
- **Performance Metrics**: Game metrics like `radiant_win`, `gold advantage`, `comeback`, and `stomp`

### Example Data

Sample data is in JSON format with fields such as:

```json
{
    "id": 1,
    "name": "npc_dota_hero_antimage",
    "primary_attr": "agi",
    "attack_type": "Melee",
    "roles": ["Carry", "Escape", "Nuker"],
    "base_health": 120,
    "base_mana": 75,
    ...
}
```
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AdityaHegde23/Dota-Stats.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Dota-Stats
   ```

3. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv env
   source env/bin/activate # For MacOS/Linux
   env\Scripts\activate    # For Windows
   pip install -r requirements.txt
   ```

## Usage

### Fetching Data

To fetch data, use the script:

```bash
python fetch_data.py
```

You can configure the number of matches fetched and specify filters such as match ID.

### Running Analysis

After data collection, run the analysis notebook or scripts in `src/eda/` for exploratory data analysis, transformations, and visualizations.

### Data Transformation

This project uses several preprocessing steps to clean and transform data, including:

- Filtering columns
- Merging and concatenating dataframes
- Handling missing values
- Mapping `radiant_win` to `Winner: Radiant/Dire`

### Example Command for EDA

To run EDA scripts or notebooks:

```bash
jupyter notebook notebooks/eda_analysis.ipynb
```

## Project Structure

```
Dota-Stats/
│
├── data/                     # Raw and processed data
├── notebooks/                # Jupyter notebooks for EDA and analysis
├── src/                      # Source code for data fetching, processing, and analysis
│   ├── fetch_data.py         # Script for fetching match data
│   ├── data_preprocessing.py # Data transformation and cleaning
│   └── analysis.py           # Core analysis and modeling
├── README.md
└── requirements.txt          # Required libraries and dependencies
```

## Analysis

### Objectives of Analysis

1. **Hero Performance Analysis**: Study hero win rates, roles, and impact in matches.
2. **Team Metrics**: Explore team gold advantages, comeback potential, and game duration for insights on game dynamics.
3. **Predictive Modeling**: Attempt to classify winning teams based on available match data.

### Key EDA Insights

1. **Winning Trends**: Distribution of match outcomes and impact of early objectives.
2. **Hero Role Analysis**: Patterns among hero roles and their impact on match outcomes.
3. **Gold and XP Trends**: Influence of gold advantage and XP on team wins.

## Contributing

If you’d like to contribute:

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

