# PDF Outline Extractor

This project extracts the hierarchical outline (table of contents) from a PDF document. It uses a rule-based approach to identify headings based on font size, style, and other textual features.

## 🌟 Features

* Extracts headings and their hierarchical levels.
* Rule-based, no ML model required.
* Lightweight and fast.
* Dockerized for easy deployment.

## 🛠️ Setup

### Prerequisites

* Docker

### Installation

1.  Clone this repository:
    ```bash
    git clone <your-repo-url>
    cd Adobe-Hack-Gen3-round1a-main
    ```

2.  Build the Docker image:
    ```bash
    docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier
    ```

## 🏃‍♀️ Running the Extractor

To extract the outline from a PDF file, place your PDF in the `app/input` directory and run the following command:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output -network none mysolutionname:somerandomidentifier
```
