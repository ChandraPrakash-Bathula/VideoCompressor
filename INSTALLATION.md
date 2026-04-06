# VideoCompressor Installation Guide

This guide provides step-by-step instructions to install and set up VideoCompressor on your system.

## Prerequisites

Before installing VideoCompressor, ensure you have:
- Python 3.7 or higher
- pip (Python package manager)
- FFmpeg with libx264 support
- At least 1GB of free disk space

## Step-by-Step Installation

### Step 1: Install FFmpeg

FFmpeg is the core dependency for video processing.

#### Ubuntu/Debian Linux
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

Verify installation:
```bash
ffmpeg -version
ffprobe -version
```

#### CentOS/RHEL
```bash
sudo yum install -y ffmpeg
```

#### macOS (Homebrew)
```bash
brew install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
ffprobe -version
```

#### Windows

**Option 1: Using Chocolatey**
```bash
choco install ffmpeg
```

**Option 2: Manual Installation**
1. Visit https://ffmpeg.org/download.html
2. Download the Windows build
3. Extract to a folder (e.g., `C:\ffmpeg`)
4. Add the folder to your system PATH:
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", click "New"
   - Variable name: `PATH`
   - Variable value: `C:\ffmpeg\bin` (or your installation path)

Verify installation:
```bash
ffmpeg -version
ffprobe -version
```

### Step 2: Clone or Download VideoCompressor

If you haven't already cloned the repository:
```bash
git clone https://github.com/ChandraPrakash-Bathula/VideoCompressor.git
cd VideoCompressor
```

Or if you have the files already:
```bash
cd /path/to/VideoCompressor
```

### Step 3: Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage dependencies:

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install ffmpeg-python==0.2.1
pip install click==8.1.7
pip install colorama==0.4.6
pip install tqdm==4.66.1
```

### Step 5: Verify Installation

Test if everything is installed correctly:

```bash
python video_compressor.py presets
```

You should see output showing all available quality presets.

## Troubleshooting Installation

### Issue: "ffmpeg command not found"

**Solution:**
- Ensure FFmpeg is installed
- Check if FFmpeg is in your system PATH
- Restart your terminal/command prompt after installing FFmpeg

### Issue: "ModuleNotFoundError: No module named 'ffmpeg'"

**Solution:**
```bash
pip install ffmpeg-python
```

### Issue: "Unknown encoder 'libx264'"

**Solution:**
- Reinstall FFmpeg with libx264 support
- On Linux: `sudo apt-get install -y libx264-dev`
- On macOS: `brew install x264 x265`

### Issue: "Permission denied" on Linux/macOS

**Solution:**
```bash
chmod +x video_compressor.py
```

### Issue: Python not found (Windows)

**Solution:**
- Ensure Python is installed
- Check if Python is in your system PATH
- Restart command prompt after installation
- Use `python` or `python3` depending on your installation

## Quick Start

Once installation is complete, you can start compressing videos:

```bash
# Get help
python video_compressor.py --help

# Compress a single video
python video_compressor.py compress input.mp4 output.mp4

# View quality presets
python video_compressor.py presets

# Get video information
python video_compressor.py info input.mp4

# Batch compress videos
python video_compressor.py batch ./videos ./compressed
```

## System Requirements for Smooth Operation

| Type | Minimum | Recommended |
|------|---------|-------------|
| CPU | Dual-core 2GHz | Quad-core 3GHz+ |
| RAM | 2GB | 8GB+ |
| Disk Space | 2GB free | 10GB+ free |
| FFmpeg | 4.0+ | 5.0+ |
| Python | 3.7 | 3.9+ |

### Performance Notes
- **CPU**: VideoCompressor uses all available cores automatically
- **RAM**: Encoding uses ~500MB-1GB RAM for full HD videos
- **Disk**: You need at least 1.5x the original video size as free space

## Advanced Configuration

### Using a Specific FFmpeg Installation

If FFmpeg is not in your PATH, you can specify its location:

Edit `video_compressor.py` and modify the subprocess calls:
```python
cmd = ['path/to/ffmpeg', ...]
```

### Custom Encoding Parameters

To add custom FFmpeg parameters, edit the `compress_video` method in `video_compressor.py`:

```python
cmd.extend(['-tune', 'film'])  # For film content
cmd.extend(['-rc-lookahead', '60'])  # Better quality
```

## Docker Installation (Optional)

If you prefer to use Docker:

```dockerfile
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    ffmpeg

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY video_compressor.py .
ENTRYPOINT ["python3", "video_compressor.py"]
```

Build and run:
```bash
docker build -t videocompressor .
docker run -v /path/to/videos:/videos videocompressor compress /videos/input.mp4 /videos/output.mp4
```

## Getting Help

If you encounter issues:

1. Check FFmpeg installation: `ffmpeg -version`
2. Verify Python: `python --version`
3. Check dependencies: `pip list`
4. Run with verbose output: `python video_compressor.py compress input.mp4 output.mp4 -v`

For additional support:
- Check the main README.md for usage examples
- Review example usage in examples.py
- Check FFmpeg documentation: https://ffmpeg.org/documentation.html

## Next Steps

- Read the [README.md](README.md) for usage instructions
- Explore [examples.py](examples.py) for code examples
- Start compressing your videos!

---

**Happy compressing! 🎬**
