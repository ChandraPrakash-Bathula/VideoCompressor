# VideoCompressor - Quick Start Guide 🚀

Get started with VideoCompressor in 5 minutes!

## Installation (2 minutes)

### 1. Install FFmpeg

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows (Chocolatey):**
```bash
choco install ffmpeg
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python video_compressor.py presets
```

You should see the quality presets listed!

## Basic Usage (3 minutes)

### Compress a Single Video

```bash
# Simple compression (balanced quality)
python video_compressor.py compress video.mp4 video_compressed.mp4

# High quality (keep more detail)
python video_compressor.py compress video.mp4 video_hq.mp4 --quality high

# Small file size (more compression)
python video_compressor.py compress video.mp4 video_small.mp4 --quality medium
```

### Batch Compress Multiple Videos

```bash
python video_compressor.py batch ./my_videos ./compressed_videos
```

### Get Video Information

```bash
python video_compressor.py info video.mp4
```

## Quality Presets at a Glance

| Preset | Quality | Speed | Size Reduction | Use Case |
|--------|---------|-------|----------------|----------|
| **ultra_high** | Best | Slow | 20-30% | Professional work, archival |
| **high** | Great | Medium | 30-40% | High-quality storage |
| **balanced** ⭐ | Good | Medium | 40-50% | **Recommended for most** |
| **medium** | Fair | Fast | 50-60% | Social media, quick share |
| **low** | Basic | Very Fast | 60-70% | Max compression |

## Command Examples

### Example 1: Quick Compression for Sharing
```bash
python video_compressor.py compress movie.mp4 movie_share.mp4 --quality medium
```
Reduces file by 50-60% in minutes.

### Example 2: High-Quality Archive
```bash
python video_compressor.py compress footage.mov archive.mp4 --quality high
```
Maintains professional quality while reducing size.

### Example 3: Batch Process with Custom Settings
```bash
python video_compressor.py batch ./raw_footage ./final_videos --quality balanced
```
Compress 100 videos automatically with balanced settings.

### Example 4: Use Different Audio Codec
```bash
python video_compressor.py compress video.mp4 video_mp3.mp4 --audio mp3
```
Audio options: `aac` (default), `mp3`, `opus`, `copy` (original)

## What to Expect

### File Size Reductions
- **MP4 (H.264)**: 40-50% with balanced quality
- **AVI files**: 60-70% with balanced quality
- **MOV files**: 50-60% with balanced quality

### Encoding Time (Approximate)
- **1 Hour Video, Balanced**: 10-30 minutes
- **4K Video, Balanced**: 30-60 minutes
- **Time varies**: Based on CPU, video resolution, codec

### Quality Preservation
- **Balanced preset**: Visually indistinguishable from original for most content
- **High preset**: Imperceptible quality loss, suitable for professional work
- **Medium preset**: Slight quality loss, still good for most purposes

## Common Scenarios

### 📱 Before Uploading to Social Media
```bash
python video_compressor.py compress video.mp4 video_web.mp4 --quality medium --audio mp3
```

### 💾 Archiving Old Videos
```bash
python video_compressor.py compress old_video.avi archive.mp4 --quality high --audio copy
```

### 🎬 Backup with Quality
```bash
python video_compressor.py compress footage.mov backup.mp4 --quality ultra_high
```

### ⚡ Maximum Compression
```bash
python video_compressor.py compress video.mp4 tiny_video.mp4 --quality low
```

## Troubleshooting

### "FFmpeg not found"
- Install FFmpeg (see Installation section above)
- Restart your terminal after installing

### "Unknown codec 'libx264'"
```bash
# On Linux
sudo apt-get install libx264-dev libx265-dev

# On macOS
brew install x264 x265
```

### Slow encoding
- Use higher quality preset for faster encoding
- Close other applications to free up CPU

### Out of disk space
- Ensure 1.5x the original file size is available as free space

## Next Steps

- 📖 Read the full [README.md](README.md) for detailed documentation
- 💡 Check [examples.py](examples.py) for Python API usage
- 🔧 See [INSTALLATION.md](INSTALLATION.md) for advanced setup options
- ⚙️ View [config.json](config.json) for quality preset details

## Tips & Tricks

1. **Test First**: Try `--quality medium` before committing to long encodes
2. **Batch Processing**: Compress videos overnight with batch mode
3. **Audio Format**: Use `--audio copy` to skip audio re-encoding (faster)
4. **Storage**: Compress old videos to free up storage space
5. **Backup**: Keep originals until satisfied with results

## Performance Example

Compressing a 2GB movie file:
```
Original: 2000 MB
Compressed (balanced): 1000 MB
Time taken: ~20 minutes (on 6-core CPU)
Quality: Visually identical to original
```

## Need Help?

```bash
# Show all commands
python video_compressor.py --help

# Show quality presets
python video_compressor.py presets

# Get info about a video
python video_compressor.py info your_video.mp4
```

---

**You're ready to start compressing! 🎬**

Start with: `python video_compressor.py compress input.mp4 output.mp4`
