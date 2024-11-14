from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from src.schema.User import User
from src.schema.Video import Video
from src.schema.Topic import Topic
from src.schema.Section import Section
from src.schema.Course import Course
from src.schema.CourseTopicAssociation import CourseTopicAssociation
from src.schema.SectionVideoAssociation import SectionVideoAssociation
