# ItchSaleSentry

ItchSaleSentry is a Python script that autonomously tracks and notifies users of items, including games and more, on the Itch.io platform when they become temporarily available for free due to limited-time sales or discounts, consistently reaching a 100% discount. Stay updated on the latest opportunities with automated Discord notifications, brought to you by ItchSaleSentry.

## Table of Contents

- [Data Source](#data-source)
- [Acknowledgment](#acknowledgment)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Data Source

The script tracks data from [freetchio](https://shaigrorb.github.io/freetchio/), a website dedicated to providing information about free items on Itch.io.

## Acknowledgment

Special thanks to [ShaigroRB](https://github.com/shaigrorb) for making the data source publicly accessible, enabling the project to track Itch.io items.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during installation.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/xAbdoATx/Itch-Sale-Sentry.git

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Configuration

To configure ItchSaleSentry, follow these steps:

1. Open the `config.json` file.

2. Customize the configuration based on your preferences:

   - **`webhook_name`**: The name to display for your Discord webhook. *(Optional)*

   - **`webhook_image`**: The image URL to display for your Discord webhook. *(Optional)*

   - **`track_url`**: The URL of the JSON file containing the items to track. *(Recommended not to change unless you have a specific JSON file you want to use.)*

   - **`webhook_url`**: Replace "YOUR_DISCORD_WEBHOOK_URL" with the actual Discord webhook URL you want to use for notifications.

This step ensures that the script is tailored to your preferences and connected to the correct Discord webhook for notifications. Adjust the values accordingly to match your desired setup.

## Dependencies

ItchSaleSentry relies on the following external libraries. You can install them manually or use the `pip install -r requirements.txt` command:

- **[discord-webhook](https://pypi.org/project/discord-webhook/)**:
  ```bash
  pip install discord-webhook

- **requests**:
  ```bash
  pip install requests

Make sure to install these dependencies to ensure the proper functioning of ItchSaleSentry. If you prefer, you can also use the pip install -r requirements.txt command to install all dependencies at once.

## Usage
- Run the script by executing the following command:

  ```bash
  python main.py
The script will start tracking Itch.io for free items and send Discord notifications for new discoveries.

![ItchSaleSentry2](https://github.com/xAbdoATx/Itch-Sale-Sentry/assets/160148781/1c2cd69f-e299-46ad-acac-48e4c000abfe)

![ItchSaleSentry1](https://github.com/xAbdoATx/Itch-Sale-Sentry/assets/160148781/397dac47-6f40-43b2-9fba-c4b27d0c2653)


## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
