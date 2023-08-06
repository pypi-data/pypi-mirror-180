# namespaces defined in XML and to be ignored in procecssing
import os.path

ignore_namespace = []

def  get_entity_addr(addr):
    if not addr: return None
    return ("%s %s %s" % (addr.AddressLine, addr.Town, addr.Postcode)).replace("None", "").strip()

def  get_entity_name(name):
    if not name: return
    if name.OrganizationName: return name.OrganizationName
    return "%s %s" % (name.FirstName, name.LastName )

def  get_entity_kind(name):
    if not name: return
    if name.OrganizationName: return 'Legal Entity'
    return 'Natural Person'

def parse_img_path(value):
    return os.path.basename(value)

# -------------------------------------------------------------
# data translation helpers:
# translate values from office interpretation to gbd equivalent
# -------------------------------------------------------------
def translate_kind(kind):
    if kind == 'Individual': return ['Individual']
    if kind == 'Collective': return ['Collective']
    if kind == 'State property': return ['Collective']
    if kind == 'Certificate': return ['Certificate']

    raise Exception('kind "%s" is not mapped.' % kind)


def translate_status(status):
    if not status: return 'Unknown'
    if status == 'Registration cancelled': return 'Expired'
    if status == 'Expired': return 'Expired'
    if status == 'Registration surrendered': return 'Expired'

    if status in [ 'Registered','Registration renewed']:
        return 'Registered'
    if status in ['DO-NOT-DISPLAY']:
        return 'Deleted'
    if status in [ 'Cancelled','Merged' ,'Removed', 'Withdrawn','Refused','Surrendered',
                   'Dead', ]:
        return 'Ended'

    if status in [ 'Application Published',
                   'Pre-Publication',
                   'Examination',
                   'Application Received',
                   'Opposed',
                   'Opposition pending',
                   'Appeal pending' ]:
        return 'Pending'

    raise Exception('Status "%s" unmapped' % status)

def sanitize(value):
    return value.replace('\n', '')

def translate_feature(feature):
    if not feature: return 'Undefined'
    if feature == 'Hologram': return 'Hologram'
    if feature == 'Motion': return 'Motion'
    if feature == 'Olfactory': return 'Olfactory'
    if feature == 'Multimedia': return 'Multimedia'
    if feature == 'Other': return 'Other'
    if feature == 'Pattern': return 'Pattern'
    if feature == 'Undefined': return 'Undefined'
    if feature == 'Word': return 'Word'
    if feature == 'Figurative': return 'Figurative'
    if feature == 'Combined': return 'Combined'
    if feature == '3-D': return 'Three dimensional'
    if feature == 'Sound': return 'Sound'
    if feature == 'Colour': return 'Colour'
    raise Exception('Feature "%s" unmapped' % feature)
