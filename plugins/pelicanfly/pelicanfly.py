import sys
from pelican import signals
from fontawesome_markdown import FontAwesomeExtension

def add_md_ext_and_static(peli):
    md_ext = peli.settings.get('MD_EXTENSIONS')
    cls = FontAwesomeExtension
    inst = cls()

    try:
        if isinstance(peli.settings.get('MD_EXTENSIONS'), list): # pelican 3.6.3 and earlier
            peli.settings['MD_EXTENSIONS'].append(inst)
        else:
            peli.settings['MARKDOWN'].setdefault('extensions', []).append(inst)
    except:
        sys.excepthook(*sys.exc_info())
        sys.stderr.write("\nError - the fontawesome_markdown extension failed to configure.\n")
        sys.stderr.flush()

def register():
    signals.initialized.connect(add_md_ext_and_static)



