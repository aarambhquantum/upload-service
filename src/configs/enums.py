import enum

class VideoTranscodingStatusEnum(enum.Enum):
  PENDING = "pending"
  PROCESSING = "processing"
  FAILED = "failed"
  COMPLETED = "completed"