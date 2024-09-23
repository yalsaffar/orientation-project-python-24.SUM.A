# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass, field


@dataclass
class Experience:
    '''
    Experience Class
    '''
    title: str = field(default="")
    company: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    description: str = field(default="")
    logo: str = field(default="")
    id: int = field(default=1)


@dataclass
class Education:
    '''
    Education Class
    '''
    course: str = field(default="")
    school: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    grade: str = field(default="")
    logo: str = field(default="")
    id: int = field(default=1)


@dataclass
class Skill:
    '''
    Skill Class
    '''
    name: str
    proficiency: str
    logo: str

@dataclass
class SocialMedia:
    '''
    Social Media Class
    '''
    linkedin: str = field(default="")
    github: str = field(default="")
    twitter: str = field(default="")
    portfolio: str = field(default="")
    email: str = field(default="")
    phone: str = field(default="")
    id: int = field(default=1)


@dataclass
class PersonalInfo:
    '''
    Personal Info Class
    '''
    name: str = field(default="")
    address: str = field(default="")
    year_of_birth: str = field(default="")
    id: int = field(default=1)
