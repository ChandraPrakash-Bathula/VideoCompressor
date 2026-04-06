#!/usr/bin/env python3
"""
Example usage of the VideoCompressor class as a Python module.
Demonstrates all major features and use cases.
"""

from video_compressor import VideoCompressor
import os


def example_1_basic_compression():
    """Example 1: Basic compression with default settings."""
    print("\n" + "="*60)
    print("Example 1: Basic Compression")
    print("="*60)
    
    compressor = VideoCompressor()
    
    # Compress a video with default balanced quality
    result = compressor.compress_video(
        input_path='sample_video.mp4',
        output_path='sample_video_compressed.mp4'
    )
    
    if result:
        print("✓ Compression successful!")
    else:
        print("✗ Compression failed!")


def example_2_high_quality_compression():
    """Example 2: High quality compression (better quality, larger file)."""
    print("\n" + "="*60)
    print("Example 2: High Quality Compression")
    print("="*60)
    
    compressor = VideoCompressor()
    
    result = compressor.compress_video(
        input_path='sample_video.mp4',
        output_path='sample_video_high_quality.mp4',
        quality='high',
        audio_codec='aac'
    )
    
    if result:
        print("✓ High quality compression successful!")


def example_3_medium_compression():
    """Example 3: Medium quality compression (social media friendly)."""
    print("\n" + "="*60)
    print("Example 3: Medium Quality Compression")
    print("="*60)
    
    compressor = VideoCompressor()
    
    result = compressor.compress_video(
        input_path='sample_video.mp4',
        output_path='sample_video_medium.mp4',
        quality='medium',
        audio_codec='mp3'
    )
    
    if result:
        print("✓ Medium quality compression successful!")


def example_4_batch_compression():
    """Example 4: Batch compress multiple videos."""
    print("\n" + "="*60)
    print("Example 4: Batch Compression")
    print("="*60)
    
    compressor = VideoCompressor()
    
    # Create sample directories
    os.makedirs('input_videos', exist_ok=True)
    os.makedirs('output_videos', exist_ok=True)
    
    # Batch compress all videos in input_videos directory
    successful = compressor.batch_compress(
        input_dir='input_videos',
        output_dir='output_videos',
        quality='balanced',
        audio_codec='aac'
    )
    
    print(f"\nSuccessfully compressed {successful} videos!")


def example_5_get_video_info():
    """Example 5: Get detailed information about a video."""
    print("\n" + "="*60)
    print("Example 5: Get Video Information")
    print("="*60)
    
    compressor = VideoCompressor()
    
    # Get video metadata
    info = compressor.get_video_info('sample_video.mp4')
    
    if info:
        print("Video Information:")
        print(f"  Format: {info.get('format', {}).get('format_name', 'Unknown')}")
        print(f"  Duration: {float(info.get('format', {}).get('duration', 0)):.2f} seconds")
        print(f"  Bit Rate: {info.get('format', {}).get('bit_rate', 'Unknown')} bps")
        
        # Display stream information
        streams = info.get('streams', [])
        for stream in streams:
            if stream.get('codec_type') == 'video':
                print(f"\nVideo Stream:")
                print(f"  Codec: {stream.get('codec_name', 'Unknown')}")
                print(f"  Resolution: {stream.get('width', 'Unknown')}x{stream.get('height', 'Unknown')}")
                print(f"  Frame Rate: {stream.get('r_frame_rate', 'Unknown')}")
            elif stream.get('codec_type') == 'audio':
                print(f"\nAudio Stream:")
                print(f"  Codec: {stream.get('codec_name', 'Unknown')}")
                print(f"  Sample Rate: {stream.get('sample_rate', 'Unknown')} Hz")
                print(f"  Channels: {stream.get('channels', 'Unknown')}")


def example_6_get_file_size():
    """Example 6: Get file size information."""
    print("\n" + "="*60)
    print("Example 6: Get File Size")
    print("="*60)
    
    compressor = VideoCompressor()
    
    size_bytes, size_str = compressor.get_file_size('sample_video.mp4')
    
    print(f"File: sample_video.mp4")
    print(f"Size: {size_str}")
    print(f"Size in bytes: {size_bytes:,}")


def example_7_compare_quality_presets():
    """Example 7: Compare different quality presets."""
    print("\n" + "="*60)
    print("Example 7: Compare Quality Presets")
    print("="*60)
    
    compressor = VideoCompressor()
    
    print("\nAvailable Quality Presets:")
    print("-" * 60)
    
    for preset_name, preset_config in compressor.QUALITY_PRESETS.items():
        print(f"\n{preset_name.upper()}")
        print(f"  CRF: {preset_config['crf']}")
        print(f"  Preset: {preset_config['preset']}")
        print(f"  Description: {preset_config['description']}")


def example_8_audio_codec_options():
    """Example 8: Demonstrate different audio codec options."""
    print("\n" + "="*60)
    print("Example 8: Audio Codec Options")
    print("="*60)
    
    compressor = VideoCompressor()
    
    print("\nAvailable Audio Codecs:")
    print("-" * 60)
    
    for codec_name, codec_config in compressor.AUDIO_CODECS.items():
        print(f"\n{codec_name.upper()}")
        print(f"  Codec: {codec_config['codec']}")
        if codec_config['bitrate']:
            print(f"  Bitrate: {codec_config['bitrate']}")


def example_9_progressive_compression():
    """Example 9: Create multiple compressed versions with different qualities."""
    print("\n" + "="*60)
    print("Example 9: Progressive Compression (Multiple Versions)")
    print("="*60)
    
    compressor = VideoCompressor()
    
    qualities = ['high', 'balanced', 'medium']
    
    for quality in qualities:
        output_file = f'sample_video_{quality}.mp4'
        print(f"\nCompressing with {quality} quality...")
        
        result = compressor.compress_video(
            input_path='sample_video.mp4',
            output_path=output_file,
            quality=quality
        )
        
        if result:
            size_bytes, size_str = compressor.get_file_size(output_file)
            print(f"✓ Created {output_file} ({size_str})")


def example_10_custom_workflow():
    """Example 10: Custom workflow with error handling."""
    print("\n" + "="*60)
    print("Example 10: Custom Workflow with Error Handling")
    print("="*60)
    
    compressor = VideoCompressor()
    
    input_video = 'sample_video.mp4'
    output_video = 'sample_video_final.mp4'
    
    # Check if input exists
    if not os.path.exists(input_video):
        print(f"✗ Input video not found: {input_video}")
        return
    
    # Get original size
    orig_size_bytes, orig_size_str = compressor.get_file_size(input_video)
    print(f"Original size: {orig_size_str}")
    
    # Get video info
    info = compressor.get_video_info(input_video)
    print(f"Duration: {float(info.get('format', {}).get('duration', 0)):.2f} seconds")
    
    # Compress
    print("\nCompressing...")
    result = compressor.compress_video(
        input_path=input_video,
        output_path=output_video,
        quality='balanced',
        audio_codec='aac'
    )
    
    if result:
        # Compare sizes
        comp_size_bytes, comp_size_str = compressor.get_file_size(output_video)
        reduction = ((orig_size_bytes - comp_size_bytes) / orig_size_bytes) * 100
        
        print(f"\nResults:")
        print(f"  Original: {orig_size_str}")
        print(f"  Compressed: {comp_size_str}")
        print(f"  Reduction: {reduction:.1f}%")


if __name__ == '__main__':
    print("VideoCompressor - Example Usage Guide")
    print("=" * 60)
    print("\nThis script demonstrates various ways to use the VideoCompressor class.")
    print("\nTo run specific examples, uncomment them below:")
    print("\n" + "=" * 60)
    
    # Uncomment any example to run it:
    # example_1_basic_compression()
    # example_2_high_quality_compression()
    # example_3_medium_compression()
    # example_4_batch_compression()
    # example_5_get_video_info()
    # example_6_get_file_size()
    # example_7_compare_quality_presets()
    # example_8_audio_codec_options()
    # example_9_progressive_compression()
    # example_10_custom_workflow()
    
    # Show help
    print("\nTo use the VideoCompressor CLI, run:")
    print("  python video_compressor.py --help")
    print("\nOr use as a Python module:")
    print("  from video_compressor import VideoCompressor")
