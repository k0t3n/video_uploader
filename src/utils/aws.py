import boto3
from django.conf import settings


def get_mediaconvert_client():
    return boto3.client(
        service_name='mediaconvert',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
        endpoint_url=settings.AWS_MEDIACONVERT_ENDPOINT_URL
    )


def generate_mediaconvert_encode_job_config(file_url):
    return {
        'Role': settings.AWS_MEDIACONVERT_ROLE,
        'Settings': {
            'TimecodeConfig': {
                'Source': 'ZEROBASED'
            },
            'OutputGroups': [
                {
                    'CustomName': 'Encoding',
                    'Name': 'File Group',
                    'Outputs': [
                        {
                            'ContainerSettings': {
                                'Container': 'MP4',
                                'Mp4Settings': {
                                    'CslgAtom': 'INCLUDE',
                                    'CttsVersion': 0,
                                    'FreeSpaceBox': 'EXCLUDE',
                                    'MoovPlacement': 'PROGRESSIVE_DOWNLOAD',
                                    'AudioDuration': 'DEFAULT_CODEC_DURATION'
                                }
                            },
                            'VideoDescription': {
                                'Width': 640,
                                'ScalingBehavior': 'DEFAULT',
                                'Height': 360,
                                'TimecodeInsertion': 'DISABLED',
                                'AntiAlias': 'ENABLED',
                                'Sharpness': 50,
                                'CodecSettings': {
                                    'Codec': 'H_264',
                                    'H264Settings': {
                                        'InterlaceMode': 'PROGRESSIVE',
                                        'ScanTypeConversionMode': 'INTERLACED',
                                        'NumberReferenceFrames': 3,
                                        'Syntax': 'DEFAULT',
                                        'Softness': 0,
                                        'GopClosedCadence': 1,
                                        'GopSize': 90,
                                        'Slices': 1,
                                        'GopBReference': 'DISABLED',
                                        'SlowPal': 'DISABLED',
                                        'EntropyEncoding': 'CABAC',
                                        'Bitrate': 1000000,
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE',
                                        'RateControlMode': 'VBR',
                                        'CodecProfile': 'MAIN',
                                        'Telecine': 'NONE',
                                        'MinIInterval': 0,
                                        'AdaptiveQuantization': 'AUTO',
                                        'CodecLevel': 'AUTO',
                                        'FieldEncoding': 'PAFF',
                                        'SceneChangeDetect': 'ENABLED',
                                        'QualityTuningLevel': 'SINGLE_PASS',
                                        'FramerateConversionAlgorithm': 'DUPLICATE_DROP',
                                        'UnregisteredSeiTimecode': 'DISABLED',
                                        'GopSizeUnits': 'FRAMES',
                                        'ParControl': 'INITIALIZE_FROM_SOURCE',
                                        'NumberBFramesBetweenReferenceFrames': 2,
                                        'RepeatPps': 'DISABLED',
                                        'DynamicSubGop': 'STATIC'
                                    }
                                },
                                'AfdSignaling': 'NONE',
                                'DropFrameTimecode': 'ENABLED',
                                'RespondToAfd': 'NONE',
                                'ColorMetadata': 'INSERT'
                            },
                            'AudioDescriptions': [
                                {
                                    'AudioTypeControl': 'FOLLOW_INPUT',
                                    'CodecSettings': {
                                        'Codec': 'AAC',
                                        'AacSettings': {
                                            'AudioDescriptionBroadcasterMix': 'NORMAL',
                                            'Bitrate': 96000,
                                            'RateControlMode': 'CBR',
                                            'CodecProfile': 'LC',
                                            'CodingMode': 'CODING_MODE_2_0',
                                            'RawFormat': 'NONE',
                                            'SampleRate': 48000,
                                            'Specification': 'MPEG4'
                                        }
                                    },
                                    'LanguageCodeControl': 'FOLLOW_INPUT'
                                }
                            ],
                        },
                        {
                            'VideoDescription': {
                                'ScalingBehavior': 'DEFAULT',
                                'TimecodeInsertion': 'DISABLED',
                                'AntiAlias': 'ENABLED',
                                'Sharpness': 50,
                                'CodecSettings': {
                                    'Codec': 'VP8',
                                    'Vp8Settings': {
                                        'QualityTuningLevel': 'MULTI_PASS',
                                        'RateControlMode': 'VBR',
                                        'GopSize': 90,
                                        'Bitrate': 1000000,
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE',
                                        'FramerateConversionAlgorithm': 'DUPLICATE_DROP',
                                        'ParControl': 'INITIALIZE_FROM_SOURCE'
                                    }
                                },
                                'DropFrameTimecode': 'ENABLED',
                                'ColorMetadata': 'INSERT',
                                'Width': 640,
                                'Height': 360
                            },
                            'AudioDescriptions': [
                                {
                                    'AudioTypeControl': 'FOLLOW_INPUT',
                                    'CodecSettings': {
                                        'Codec': 'OPUS',
                                        'OpusSettings': {
                                            'Bitrate': 96000,
                                            'Channels': 2,
                                            'SampleRate': 48000
                                        }
                                    },
                                    'LanguageCodeControl': 'FOLLOW_INPUT'
                                }
                            ],
                            'ContainerSettings': {
                                'Container': 'WEBM'
                            }
                        },
                    ],
                    'OutputGroupSettings': {
                        'Type': 'FILE_GROUP_SETTINGS',
                        'FileGroupSettings': {
                            'Destination': f'{settings.AWS_S3_MEDIA_PATH}/{settings.ENCODED_VIDEOS_DIR}/'
                        }
                    }
                },
                {
                    'CustomName': 'Thumbnails',
                    'Name': 'File Group',
                    'Outputs': [
                        {
                            'ContainerSettings': {
                                'Container': 'RAW'
                            },
                            'VideoDescription': {
                                'Width': 640,
                                'ScalingBehavior': 'DEFAULT',
                                'Height': 360,
                                'TimecodeInsertion': 'DISABLED',
                                'AntiAlias': 'ENABLED',
                                'Sharpness': 50,
                                'CodecSettings': {
                                    'Codec': 'FRAME_CAPTURE',
                                    'FrameCaptureSettings': {
                                        'FramerateNumerator': 1,
                                        'FramerateDenominator': 5,
                                        'MaxCaptures': 1,
                                        'Quality': 80
                                    }
                                },
                                'DropFrameTimecode': 'ENABLED',
                                'ColorMetadata': 'INSERT'
                            }
                        }
                    ],
                    'OutputGroupSettings': {
                        'Type': 'FILE_GROUP_SETTINGS',
                        'FileGroupSettings': {
                            'Destination': f'{settings.AWS_S3_MEDIA_PATH}/{settings.THUMBNAILS_DIR}/'
                        }
                    }
                }
            ],
            'AdAvailOffset': 0,
            'Inputs': [
                {
                    'AudioSelectors': {
                        'Audio Selector 1': {
                            'Offset': 0,
                            'DefaultSelection': 'DEFAULT',
                            'ProgramSelection': 1
                        }
                    },
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW',
                        'Rotate': 'DEGREE_0',
                        'AlphaBehavior': 'DISCARD'
                    },
                    'FilterEnable': 'AUTO',
                    'PsiControl': 'USE_PSI',
                    'FilterStrength': 0,
                    'DeblockFilter': 'DISABLED',
                    'DenoiseFilter': 'DISABLED',
                    'InputScanType': 'AUTO',
                    'TimecodeSource': 'ZEROBASED',
                    'FileInput': file_url
                }
            ]
        },
        'AccelerationSettings': {
            'Mode': 'DISABLED'
        },
        'StatusUpdateInterval': 'SECONDS_60',
        'Priority': 0
    }
