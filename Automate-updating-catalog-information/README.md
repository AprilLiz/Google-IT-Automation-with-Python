# Process Sales Data and Upload it to Running Web Service + Check Health Status of System

This script: 
- summarizes and processes sales data into different categories; 
- uploads sales data to web service;
- generates a PDF sales report using Python and automatically sends it by email;
- automatically monitors the health status of the system and sends a warning email if there's an issue. 

## Usage

### Convert supplier images from TIFF to JPEG format

```bash
./changeImage.py
```

### Upload sales images to web server

```bash
./supplier_image_upload.py
```

### Upload sales descriptions to web server

```bash
./run.py
```

### Generate a PDF sales report and send it through email

```bash
./report_email.py
```

### Check some of the system statistics: CPU usage, disk space, available memory and name resolution and send an email if there are problems

```bash
./health_check.py
```
### Set a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user

```bash
./crontab_file
```