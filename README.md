
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

## Features

- **Image Compressor**: Upload an image, select the compression quality, and download the compressed image.
- **Image Enhancer**: Upload an image, choose a scale factor to increase its resolution, and download the enhanced image.
- **QR Code Generator**: Enter text to generate a QR code, view it, and download the QR code image.
- **URL Shortener**: Shorten long URLs and get a short link that redirects to the original URL.
- **File Converter**: Convert images to PDFs, DOCX files to text, and JSON files to text.

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

## Demo

You can try out the app by visiting the following URLs:
- [Image Compressor](http://localhost:5000/image_compressor)
- [Image Enhancer](http://localhost:5000/image_upscaler)
- [QR Code Generator](http://localhost:5000/qr_code)
- [URL Shortener](http://localhost:5000/url_shortener)
- [File Converter](http://localhost:5000/file_converter)

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