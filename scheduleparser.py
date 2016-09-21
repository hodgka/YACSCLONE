import urllib2
import xml.etree.cElementTree as ET
import requests
import xmltodict
import pickle



class Schedule:
    def __init__(self, crns=None, courses=None, credits=None, times=None):
        self.crns = crns
        self.courses = courses
        self.credits = credits
        self.class_times = times

    def get_crns(self):
        return self.crns

    def get_courses(self):
        return self.courses

    def get_credits(self):
        return self.credits

    def get_class_times(self):
        return self.class_times

    def set_crns(self, crns):
        self.crns = crns

    def set_courses(self, courses):
        self.courses = courses

    def set_class_times(self, class_times):
        self.class_times = class_times


class Course:
    def __init__(self, department_name=None, course_name=None,
                 course_number=None, credits=None, gradetype='',
                 crosslistings=None, description=None, sections=None,
                 semesters_offered=None, total_seats=None):
        self.department_name = department_name
        self.course_name = course_name
        self.course_number = course_number
        self.credits = credits
        self.gradetype = gradetype
        self.crosslistings = crosslistings
        self.description = description
        self.sections = sections
        self.semesters_offered = semesters_offered
        self.total_seats = total_seats

    def __repr__(self):
        return "department: {0}, course_name: {1}, course_number: {2},\
                credits: {3}, gradetype: {4}, crosslistings: {5},\
                description: {6}, sections: {7},\
                semesters_offered: {8}, total_seats: {9}\
                ".format(self.department_name, self.course_name,
                         self.course_number, self.credits, self.gradetype,
                         self.crosslistings, self.description,
                         self.sections, self.semesters_offered,
                         self.total_seats)

    def get_department(self):
        return self.department_name

    def get_course_name(self):
        return self.course_name

    def get_course_number(self):
        return self.course_number

    def get_credits(self):
        return self.credits

    def get_grade_type(self):
        return gradetype

    def get_crosslistings(self):
        return self.crosslistings

    def get_description(self):
        return self.description

    def get_sections(self):
        return self.sections

    def get_semesters(self):
        return self.semesters_offered

    def get_total_seats(self):
        return self.total_seats

    def set_department(self, dept):
        self.dept = dept

    def set_course_name(self, name):
        self.course_name = name

    def set_course_number(self, num):
        self.course_number = num

    def set_grade_type(self, gradetype):
        self.dept = new_dept

    def set_crosslistings(self, crns):
        self.crosslistings = crns

    def set_description(self, description):
        self.description = description

    def set_sections(self, sections):
        self.sections = sections

    def set_semesters(self, semesters):
        self.semesters_offered = semesters

    def set_total_seats(self, seats):
        self.total_seats = seats


class Section:
    def __init__(self, crn=None, num=None, enrolled=None, seats=None,
                 days=None, periods=None, notes=None):
        self.crn = crn
        self.section_number = num
        self.number_enrolled = enrolled
        self.seats = seats
        self.days = days
        self.periods = periods
        self.notes = notes

    def __repr__(self):
        return "crn: {0}, section_number: {1}, number_enrolled: {2},seats: {3}, days: {4}, periods: {5}".format(self.crn, self.section_number, self.number_enrolled,
                         self.seats, self.days, self.periods)

    def __str__(self):
        return "crn: {0}, section_number: {1}, number_enrolled: {2},seats: {3}, days: {4}, periods: {5}".format(self.crn, self.section_number, self.number_enrolled,
                         self.seats, self.days, self.periods)

    def get_crn(self):
        return self.crn

    def get_section_number(self):
        return self.section_number

    def get_number_enrolled(self):
        return self.number_enrolled

    def get_seats(self):
        return self.seats

    def get_days(self):
        return self.days

    def get_periods(self):
        return self.periods

    def get_notes(self):
        return self.notes

    def set_crn(self, crn):
        self.crn = crn

    def set_section_number(self, num):
        self.section_number = num

    def set_enrolled(self, enrolled):
        self.number_enrolled = enrolled

    def set_seats(self, seats):
        self.seats = seats

    def set_days(self, days):
        if self.days is None:
            self.days = days
        elif type(days) is list:
            for day in days:
                if day not in self.days:
                    self.days.append(day)
        else:
            if days not in self.days:
                self.days.append(days)

    def set_periods(self, periods):
        if self.periods == None:
            self.periods = [periods]
        elif type(periods) is list:
            for period in periods:
                self.periods.append(period)
        else:
            self.periods.append(periods)

    def set_notes(self, notes):
        if self.notes == None:
            self.notes = [notes]
        elif type(notes) is list:
            for note in notes:
                self.notes.append(note)
        else:
            self.notes.append(notes)


class Period:
    def __init__(self, type=None, instructor=None, start=None, end=None,
                 location=None, day=None):
        self.type = type
        self.instructor = instructor
        self.start_time = start
        self.end_time = end
        self.location = location
        self.day = day

    def __repr__(self):
        return "type: {0}, instructor: {1}, start: {2}, end: {3},location: {4}, day: {5}".format(self.type, self.instructor,
                         self.start_time, self.end_time,
                         self.location, self.day)

    def __str__(self):
        return "type: {0}, instructor: {1}, start: {2}, end: {3},location: {4}, day: {5}".format(self.type, self.instructor,
                         self.start_time, self.end_time,
                         self.location, self.day)

    def get_type(self):
        return self.type

    def get_instructor(self):
        return self.instructor

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_location(self):
        return self.location

    def get_day(self):
        return self.day

    def set_type(self, type):
        self.type = type

    def set_instructor(self, instructor):
        self.instructor = instructor

    def set_start_time(self, time):
        self.start_time = time

    def set_end_time(self, time):
        self.end_time = time

    def set_location(self, location):
        self.location = location

    def set_day(self, day):
        if self.day == None:
            self.day = [day]
        elif type(day) is list:
            for d in day:
                self.day.append(d)
        else:
            self.day.append(day)

    def overlaps(self, p2):
        if((self.start_time < p2.get_start_time() < self.end_time) or
           (p2.get_start_time() < self.start_time < p2.get_end_time())):
            return True
            return False


class CourseListings:
    def __init__(self, courses):
        self.courses = courses




# TODO should go in a class as a method
# TODO probably will go in CourseListings
def get_class_xml(url):
    ''' gets the class schedule xml file and gets the root'''
    try:
        resp = requests.get("https://sis.rpi.edu/reg/rocs/{0}.xml"
                            .format(semester), stream=True)
        tree = et.parse(resp.raw)
        root = tree.getroot()
    except:
        raise ValueError("")
    return root


def parse_class_database(root):
    ''' takes the root node of and xml file and parses the schedule'''
    day_dict = {0: "Mon", 1: "Tues", 2: "Wed", 3: "Thurs", 4: "Fri"}
    # TODO need to fix crosslistings
    crosslistings = {}
    #generate dictionary where each crn with a crosslisting has a tuple with crosslisted classes
    for crosslisting in root.findall("CROSSLISTING"):
        crns = tuple(crn.text for crn in list(crosslisting))
        for crn in crns:
            crosslistings[crn] = crns
    all_courses = []
    # get course nodes
    for course in root.findall("COURSE"):
        course_at = course.attrib
        course_sections = []
        # get section nodes
        for section in course.findall("SECTION"):
            section_at = section.attrib
            section_periods = []
            section_notes = []
            # get period nodes
            for period in section.findall("PERIOD"):
                period_at = period.attrib
                days = period.findall("DAY")
                class_days = []
                for day in days:
                    class_days.append(day_dict[int(day.text)])
                # put everything into course, section, and period nodes
                section_periods.append(Period(type=period_at["type"],
                                    instructor=period_at["instructor"],
                                    start=period_at["start"],
                                    end=period_at["end"],
                                    location=period_at["location"],
                                    day=class_days))
                for note in section.findall("NOTES"):
                    section_notes.append(note.text)
            course_sections.append(Section(crn=section_at["crn"],
                                  num=section_at["num"],
                                  enrolled=section_at["students"],
                                  seats=section_at["seats"],
                                  periods=section_periods,
                                  notes=section_notes))
        all_courses.append(Course(department_name=course_at["dept"],
                            course_name=course_at["name"],
                            course_number=int(course_at["num"]),
                            credits=course_at["credmax"],
                            gradetype=course_at["gradetype"],
                            sections=course_sections
                            ))

    return all_courses


#----------------------------------------------------------------------
def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    resp = requests.get(xml_file, stream=True)
    # print resp

    tree = ET.parse(resp.raw)

    root = tree.getroot()
    print root

    #  for child in root:
    #     print child.tag, child.attrib
    #     if child.tag == "COURSE":
    #         for step_child in child:
    #             print step_child.tag, step_child.attrib

    # iterate over the entire tree
    # print "-" * 40
    # print "Iterating using a tree iterator"
    # print "-" * 40
    iter_ = tree.getiterator()
    for elem in iter_:
        print elem.tag, elem.attrib, elem.text
    #
    # # get the information via the children!
    # print "-" * 40
    # print "Iterating using getchildren()"
    # print "-" * 40
    # appointments = root.getchildren()
    # for appointment in appointments:
    #     appt_children = appointment.getchildren()
    #     for appt_child in appt_children:
    #         print "%s=%s" % (appt_child.tag, appt_child.text)

#----------------------------------------------------------------------
if __name__ == "__main__":

    semester = 201609
    schedule_url = "https://sis.rpi.edu/reg/rocs/{0}.xml".format(semester)
    # dbroot = get_class_xml(schedule_url)
    # db = parse_class_database(dbroot)
    # print db
    parseXML(schedule_url)
