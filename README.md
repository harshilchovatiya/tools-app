# Tools App

Welcome to the Tools App! This application provides a suite of useful tools for image processing, file conversion, URL shortening, and QR code generation.

## Overview

The Tools App includes the following features:
1. **Image Compressor**: Compresses images by adjusting their quality.
2. **Image Enhancer**: Upscales image resolution based on a scale factor.
3. **QR Code Generator**: Generates QR codes from text.
4. **URL Shortener**: Shortens long URLs to manageable short links.
5. **File Converter**: Converts various file types to different formats, including:
   - **Image to PDF**
   - **DOCX to TXT**
   - **JSON to TXT**
6. **Image to Text Converter**: Converts images to text using OCR.
7. **Speedtest**: Measures the speed of your internet connection.
8. **Unit Converter**: Converts between different units of measurement.

## Features

- **Image Compressor**: Upload an image, select the compression quality, and download the compressed image.
- **Image Enhancer**: Upload an image, choose a scale factor to increase its resolution, and download the enhanced image.
- **QR Code Generator**: Enter text to generate a QR code, view it, and download the QR code image.
- **URL Shortener**: Shorten long URLs and get a short link that redirects to the original URL.
- **File Converter**: Convert images to PDFs, DOCX files to text, and JSON files to text.
- **Image to Text Converter**: Upload an image and receive the extracted text.
- **Speedtest**: Measure your internet connection's download and upload speeds.
- **Unit Converter**: Convert between units like length, weight, and temperature.

## API Documentation

### **QR Code API**

- **Endpoint**: `/api/qr_code`
- **Method**: `POST`
- **Request**: JSON payload with `text` field.
- **Response**: JSON containing the base64-encoded QR code image.

### **URL Shortener API**

- **Endpoint**: `/api/shorten`
- **Method**: `POST`
- **Request**: JSON payload with `long_url` field.
- **Response**: JSON containing the `short_url`.

- **Endpoint**: `/api/expand/<short_url>`
- **Method**: `GET`
- **Response**: JSON containing the `long_url` or error message.

### **Image Compressor API**

- **Endpoint**: `/api/image_compressor`
- **Method**: `POST`
- **Request**: Form data with `image` file and `quality` parameter.
- **Response**: Compressed image in JPEG format.

### **Image Enhancer API**

- **Endpoint**: `/api/image_upscaler`
- **Method**: `POST`
- **Request**: Form data with `image` file and `scale` factor.
- **Response**: Upscaled image in JPEG format.

### **File Converter API**

- **Endpoint**: `/api/convert_file`
- **Method**: `POST`
- **Request**: Form data with `file`, `file_type`, and `output_format`.
- **Response**: Converted file (PDF or TXT) based on input and output format.

### **Image to Text API**

- **Endpoint**: `/api/image_to_text`
- **Method**: `POST`
- **Request**: Form data with `image` file.
- **Response**: JSON containing the extracted text.

### **Speedtest API**

- **Endpoint**: `/api/speedtest`
- **Method**: `GET`
- **Response**: JSON containing download and upload speeds.

### **Unit Converter API**

- **Endpoint**: `/api/unit_converter`
- **Method**: `POST`
- **Request**: JSON payload with `value`, `from_unit`, and `to_unit` fields.
- **Response**: JSON containing the converted value.

## API Reference

### **Generate QR Code**

```http
  POST /api/qr_code
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text`    | `string` | **Required**. Text to generate QR code |

### **Shorten URL**

```http
  POST /api/shorten
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `long_url`| `string` | **Required**. Long URL to shorten |

### **Expand URL**

```http
  GET /api/expand/<short_url>
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `short_url` | `string` | **Required**. Short URL to expand |

### **Image Compressor**

```http
  POST /api/image_compressor
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `image`   | `file`   | **Required**. Image file to compress |
| `quality` | `integer`| **Optional**. Compression quality (10-90) |

### **Image Enhancer**

```http
  POST /api/image_upscaler
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `image`   | `file`   | **Required**. Image file to upscale |
| `scale`   | `float`  | **Optional**. Scale factor for resizing (e.g., 2 for 2x) |

### **File Converter**

```http
  POST /api/convert_file
```

| Parameter     | Type     | Description                              |
| :------------ | :------- | :--------------------------------------- |
| `file`        | `file`   | **Required**. File to convert            |
| `file_type`   | `string` | **Required**. Type of the file to convert (`image`, `docx`, `json`) |
| `output_format` | `string` | **Required**. Desired output format (`pdf` or `txt`) |

### **Image to Text**

```http
  POST /api/image_to_text
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `image`   | `file`   | **Required**. Image file to extract text from |

### **Speedtest**

```http
  GET /api/speedtest
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None`    | `None`   | Returns download and upload speeds |

### **Unit Converter**

```http
  POST /api/unit_converter
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `value`   | `float`  | **Required**. Value to convert |
| `from_unit` | `string` | **Required**. Unit of the value being converted |
| `to_unit` | `string` | **Required**. Unit to convert to |

## Demo

You can try out the app by visiting the following URLs:
- [Image Compressor](http://localhost:5000/image_compressor)
- [Image Enhancer](http://localhost:5000/image_upscaler)
- [QR Code Generator](http://localhost:5000/qr_code)
- [URL Shortener](http://localhost:5000/url_shortener)
- [File Converter](http://localhost:5000/file_converter)
- [Image to Text Converter](http://localhost:5000/image_to_text)
- [Speedtest](http://localhost:5000/speedtest)
- [Unit Converter](http://localhost:5000/unit_converter)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harshilchovatiya/tools-app.git
   cd tools-app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python app.py
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000` to use the app.

## Contact

For any inquiries or issues, please contact:
- **Email**: harshilbmk@gmail.com
- **LinkedIn**: [Harshil Chovatiya](https://www.linkedin.com/in/harshilbmk)

---

Thank you for using the Tools App. Enjoy exploring and utilizing the various tools!