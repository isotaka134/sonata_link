# Sonata Link

Sonata Link is a Python script that fetches archived links from the Wayback Machine for a given website and saves them to a file. It provides options to filter links by date range and to enable verbose output.

## Features

- Fetch archived links from the Wayback Machine.
- Save the fetched links to a specified file.
- Filter results by date range.
- Verbose mode for detailed output.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

- **Clone the Repository**

   ```sh
   git clone https://github.com/isotaka134/sonata_link.git
   cd sonata_link

## Usage

- Make the script executable:

  ``` sh
  chmod +x sonata_link.py

- Move the script to a directory in your PATH (e.g: `/usr/local/bin`):

    ```sh
    sudo mv sonata_link.py /usr/local/bin/sonata_link
- Run the script using the following command:
    ```sh
    sonata_link <website> <filename> [--start-date YYYYMMDD] [--end-date YYYYMMDD] [--verbose]
## Arguments
- `<website>`: The website URL (e.g., `example.com`).
- `<filename>`: The filename to save the links (e.g. `links.txt`).
- `--start-date YYYYMMDD`: Start date for filtering (optional).
- `--end-date YYYYMMDD`: End date for filtering (optional).
- `--verbose`: Enable verbose output (optional).

## Example

```sh
sonata_link example.com links.txt --start-date 20200101 --end-date 20201231 --verbose

```
This command fetches archived links for `example.com` between January 1, 2020, and December 31, 2020, and saves them to `links.txt` with detailed output.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

