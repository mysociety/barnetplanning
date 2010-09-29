__auth__ = None

import re

date_format = "%d/%m/%Y"

def fixNewlines(text):
    # This can be used to sort out windows newlines
    return text.replace("\r\n","\n")

# So what can a postcode look like then?
# This list of formats comes from http://www.mailsorttechnical.com/frequentlyaskedquestions.cfm
#AN NAA  	M1 1AA
#ANN NAA 	M60 1NW
#AAN NAA 	CR2 6XH
#AANN NAA 	DN55 1PT
#ANA NAA 	W1A 1HP
#AANA NAA 	EC1A 1BB

postcode_regex = re.compile("[A-Z][A-Z]?\d(\d|[A-Z])? ?\d[A-Z][A-Z]")

def getPostcodeFromText(text, default_postcode="No Postcode"):
    """This function takes a piece of text and returns the first
    bit of it that looks like a postcode."""

    postcode_match = postcode_regex.search(text)

    return postcode_match.group() if postcode_match else default_postcode


class PlanningAuthorityResults:
    """This class represents a set of results of a planning search.

       This should probably be separated out so that it can be used for
       authorities other than Cherwell.
       """

    def __init__(self, authority_name, authority_short_name):
	self.authority_name = authority_name
	self.authority_short_name = authority_short_name
	
	# this will be a list of PlanningApplication objects
	self.planning_applications = []


    def addApplication(self, application):
	self.planning_applications.append(application)

    def __repr__(self):
	return self.displayXML()
        
    def displayXML(self):
        """This should display the contents of this object in the planningalerts format.
           i.e. in the same format as this one:
           http://www.planningalerts.com/lambeth.xml
           """

	applications_bit = "".join([x.displayXML() for x in self.planning_applications])

	return u"""<?xml version="1.0" encoding="UTF-8"?>\n""" + \
            u"<planning>\n" +\
            u"<authority_name>%s</authority_name>\n" %self.authority_name +\
            u"<authority_short_name>%s</authority_short_name>\n" %self.authority_short_name +\
            u"<applications>\n" + applications_bit +\
            u"</applications>\n" +\
            u"</planning>\n"



class PlanningApplication:
    def __init__(self):
        self.council_reference = None
	self.address = None
	self.postcode = None
	self.description = None
	self.info_url = None
	self.comment_url = None

        # expecting this as a datetime.date object
	self.date_received = None

        # If we can get them, we may as well include OSGB.
        # These will be the entirely numeric version.
        self.osgb_x = None
        self.osgb_y = None

    def __repr__(self):
	return self.displayXML()

    def is_ready(self):
        # This method tells us if the application is complete
        # Because of the postcode default, we can't really
        # check the postcode - make sure it is filled in when
        # you do the address.
        return self.council_reference \
            and self.address \
            and self.description \
            and self.info_url \
            and self.comment_url \
            and self.date_received
    
        
    def displayXML(self):
        #print self.council_reference, self.address, self.postcode, self.description, self.info_url, self.comment_url, self.date_received

        if not self.postcode:
            self.postcode = getPostcodeFromText(self.address)

	contents = [
            u"<council_reference><![CDATA[%s]]></council_reference>" %(self.council_reference),
            u"<address><![CDATA[%s]]></address>" %(self.address),
            u"<postcode><![CDATA[%s]]></postcode>" %self.postcode,
            u"<description><![CDATA[%s]]></description>" %(self.description),
            u"<info_url><![CDATA[%s]]></info_url>" %(self.info_url),
            u"<comment_url><![CDATA[%s]]></comment_url>" %(self.comment_url),
            u"<date_received><![CDATA[%s]]></date_received>" %self.date_received.strftime(date_format),
            ]
        if self.osgb_x:
            contents.append(u"<osgb_x>%s</osgb_x>" %(self.osgb_x))
        if self.osgb_y:
            contents.append(u"<osgb_y>%s</osgb_y>" %(self.osgb_y))

        return u"<application>\n%s\n</application>" %('\n'.join(contents))
