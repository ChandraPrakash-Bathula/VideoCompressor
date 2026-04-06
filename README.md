# VideoCompressor 🎬

A powerful Python-based video compression tool that reduces video file sizes while maintaining video and audio quality. Built on FFmpeg, it supports all video formats and provides flexible quality presets.

## Web UI Quick Start

Run this project as a browser app:

1. Install FFmpeg (required)
2. Install Python packages:

  pip install -r requirements.txt

3. Start the web server:

  python app.py

4. Open browser:

  http://127.0.0.1:5000

5. Upload video, click Compress And Download

The compressed file downloads automatically as soon as compression finishes.

Default behavior for UI mode:
- Keeps original resolution and frame rate
- Uses H.264 with high quality preset by default
- Produces MP4 output for best compatibility
- Returns file directly as download response

## Features

✨ **Key Features:**
- 🎥 **Multiple Format Support**: Works with MP4, AVI, MKV, MOV, FLV, WMV, WebM, and more
- 🎯 **Quality Presets**: 5 preset levels from ultra-high quality to very compressed
- 🔊 **Audio Codec Options**: Support for AAC, MP3, Opus, or original audio passthrough
- 📁 **Batch Processing**: Compress multiple videos at once
- 📊 **Detailed Compression Stats**: See exact size reduction and compression ratios
- ⚡ **Intelligent Encoding**: Uses H.264 codec with optimized settings for fast encoding
- 🛡️ **Safe Defaults**: Preserves quality while achieving significant size reduction

## Requirements

- **Python 3.7+**
- **FFmpeg 4.0+** (with libx264 support)
- **ffprobe** (usually bundled with FFmpeg)

## Installation

### 1. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
Download from https://ffmpeg.org/download.html or use:
```bash
choco install ffmpeg
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install ffmpeg-python click colorama tqdm
```

### 3. Verify Installation

```bash
python video_compressor.py presets
```

## Usage

### Single Video Compression

Basic compression with default balanced quality:
```bash
python video_compressor.py compress input.mp4 output.mp4
```

With high quality preset:
```bash
python video_compressor.py compress input.mp4 output.mp4 --quality high
```

Remove original file after compression:
```bash
python video_compressor.py compress input.mp4 output.mp4 --keep-original False
```

### Batch Processing

Compress all videos in a directory:
```bash
python video_compressor.py batch ./videos ./compressed_videos
```

With specific quality level:
```bash
python video_compressor.py batch ./videos ./compressed_videos --quality medium
```

### Video Information

Get detailed information about a video:
```bash
python video_compressor.py info video.mp4
```

### Quality Presets

View all available quality presets:
```bash
python video_compressor.py presets
```

## Quality Presets Explained

### ultra_high
- **CRF**: 15 (very high quality, more detail preserved)
- **Preset**: slow (more encoding time, better compression)
- **Use Case**: Professional content, archival, when quality is critical
- **File Size**: ~20-30% reduction

### high
- **CRF**: 18 (high quality, suitable for most content)
- **Preset**: medium (balanced encoding time)
- **Use Case**: High-quality storage, streaming
- **File Size**: ~30-40% reduction

### balanced ⭐ (Default)
- **CRF**: 23 (good quality-compression balance)
- **Preset**: medium (balanced encoding time)
- **Use Case**: General purpose video compression
- **File Size**: ~40-50% reduction

### medium
- **CRF**: 28 (noticeable quality reduction)
- **Preset**: fast (quick encoding)
- **Use Case**: Social media, quick sharing
- **File Size**: ~50-60% reduction

### low
- **CRF**: 32 (significant quality reduction)
- **Preset**: veryfast (very quick encoding)
- **Use Case**: Maximum compression, temporary files
- **File Size**: ~60-70% reduction

**CRF Scale**: 0-51 (0 = lossless, 18-28 = visually lossless, 51 = worst quality)

## Audio Codec Options

- **aac** (default): High-quality audio, universal compatibility, 128 kbps
- **mp3**: Maximum compatibility, 128 kbps
- **opus**: Modern codec, excellent quality at low bitrate, 128 kbps
- **copy**: Preserve original audio without re-encoding (fastest)

## Command Line Arguments

### compress command
```
python video_compressor.py compress INPUT OUTPUT [OPTIONS]

Arguments:
  INPUT                     Input video file path
  OUTPUT                    Output video file path

Options:
  --quality {ultra_high, high, balanced, medium, low}
                            Quality preset (default: balanced)
  --audio {aac, mp3, opus, copy}
                            Audio codec (default: aac)
  --keep-original          Keep original file (default: True)
```

### batch command
```
python video_compressor.py batch INPUT_DIR OUTPUT_DIR [OPTIONS]

Arguments:
  INPUT_DIR                 Input directory containing videos
  OUTPUT_DIR                Output directory for compressed videos

Options:
  --quality {ultra_high, high, balanced, medium, low}
                            Quality preset (default: balanced)
  --audio {aac, mp3, opus, copy}
                            Audio codec (default: aac)
```

### info command
```
python video_compressor.py info VIDEO

Arguments:
  VIDEO                     Video file path
```

## Examples

### Example 1: Compress a 4K video while maintaining quality
```bash
python video_compressor.py compress 4k_video.mp4 4k_compressed.mp4 --quality high
```

### Example 2: Quickly compress for sharing (smaller file)
```bash
python video_compressor.py compress video.mp4 video_small.mp4 --quality medium
```

### Example 3: Batch compress all videos with MP3 audio
```bash
python video_compressor.py batch ./raw_videos ./compressed_videos --quality balanced --audio mp3
```

### Example 4: Archive video with best quality
```bash
python video_compressor.py compress project.mov project_archive.mp4 --quality ultra_high --audio copy
```

### Example 5: Quick compression and delete original
```bash
python video_compressor.py compress temp_video.avi temp_video.mp4 --quality low --keep-original False
```

## How It Works

1. **Codec**: Uses H.264 (libx264) - widely compatible, efficient
2. **Quality Control**: CRF (Constant Quality Rate) value for consistent quality
3. **Optimization**: 
   - Appropriate preset (ultrafast → slow) based on quality level
   - `movflags +faststart` for streaming optimization
   - Optimized audio bitrate
4. **Safety**: Validates inputs, asks before overwriting, cleans up on errors

## Performance Tips

1. **Use SSD**: Video encoding is disk-intensive
2. **Multi-Core System**: FFmpeg automatically uses all available cores
3. **Quick Preview**: Use `--quality medium` first to test settings
4. **Batch Processing**: Process multiple videos overnight
5. **Monitor Resources**: FFmpeg can use significant CPU and RAM

## Typical Size Reductions

| Format | Quality | Size Reduction |
|--------|---------|----------------|
| H.264 (MP4) | balanced | 40-50% |
| H.265 (HEVC) | balanced | 50-60% |
| AVI | balanced | 60-70% |
| MOV | balanced | 50-60% |

**Note**: Actual reductions depend on source codec, resolution, and format.

## Troubleshooting

### FFmpeg not found
```
Error: FFmpeg is not installed or not in PATH
```
**Solution**: Install FFmpeg and ensure it's in your system PATH

### Permission denied
```
PermissionError: [Errno 13] Permission denied: 'output.mp4'
```
**Solution**: Check output directory permissions or specify a different output location

### Codec not available
```
Unknown encoder 'libx264'
```
**Solution**: Reinstall FFmpeg with libx264 support

### Out of disk space
```
Error: No space left on device
```
**Solution**: Ensure sufficient disk space (at least 1.5x the original video size)

### Very slow encoding
The `slow` preset in `ultra_high` quality takes longer. Use `high` or `balanced` for faster encoding.

## Advanced Usage

### Custom FFmpeg Parameters

For advanced users, modify the `compress_video` method to add custom FFmpeg flags:
```python
cmd.extend(['-tune', 'film'])  # Optimize for film content
cmd.extend(['-rc-lookahead', '60'])  # Better quality
```

### Python API Usage

```python
from video_compressor import VideoCompressor

compressor = VideoCompressor()

# Compress a single video
compressor.compress_video(
    'input.mp4',
    'output.mp4',
    quality='high',
    audio_codec='aac'
)

# Get video information
info = compressor.get_video_info('video.mp4')

# Get file size
size_bytes, size_str = compressor.get_file_size('video.mp4')
```

## Supported Formats

**Video Formats**: MP4, AVI, MKV, MOV, FLV, WMV, WebM, 3GP, OGV, and more
**Audio Formats**: AAC, MP3, Opus (in various containers)
**Codecs**: H.264, H.265, VP8, VP9, AV1 input support

## Performance Benchmarks

On a modern CPU (6-core i7):
- **1080p 5-min video**: ~2-5 minutes (balanced quality)
- **4K 10-min video**: ~10-20 minutes (balanced quality)
- **480p YouTube**: ~30-60 seconds (medium quality)

## Limitations

- Transcoding takes time (proportional to video length)
- Very high-quality videos may not compress well
- Some codecs (like AV1) not supported for output (future enhancement)

## Future Enhancements

- [ ] H.265/HEVC codec support for better compression
- [ ] AV1 codec support
- [ ] GPU acceleration (NVIDIA NVENC, AMD VCE)
- [ ] Subtitle and metadata preservation
- [ ] Progress bar for long operations
- [ ] Web UI for ease of use
- [ ] Automatic quality selection based on content analysis

## Contributing

Contributions are welcome! Areas for improvement:
- GPU encoding support
- Additional codec options
- Performance optimizations
- Better error handling
- GUI interface

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for personal use with content you own or have permission to process. Always respect copyright laws and content creator rights.

## Support

For issues, bugs, or feature requests, please open an issue on GitHub.

---

**Made with ❤️ for video enthusiasts and content creators**
