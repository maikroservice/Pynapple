



# TODO
* plugins can be provided in YAML format
* they can either be added via CLI parameter (-p?) or directly placed into the plugins folder
* default behaviour - scan for all plugins from plugins folder 


# PLUGIN
* name
* optional: stars
* 

```yaml
id: php-lfi-include
info:
  name: PHP local file inclusion via include()
  author: maikroservice
  #severity: medium
  description: searching for PHP local file inclusion because of include() use
  tags:
    - php
    - lfi
    - include
parameters:
  languages: 
    - "php"
  file_types: 
    - "php"
    - "php3"
    - "php5"
    - "phps"
  matchers:
    regular_expression: True
    regex: ""
    
    # Important: Keep the proceeding three matches
    #"regex": re.compile(b"\n(.*)\n(.*)\n(.*)(INSERT YOUR REGEX HERE)",
    #    re.IGNORECASE | re.MULTILINE)
```

## SOURCES

https://dev.to/charlesw001/plugin-architecture-in-python-jla

https://wiki.gnome.org/Apps/Gedit/PythonPluginHowToOld

http://martyalchin.com/2008/jan/10/simple-plugin-framework/ 

http://yapsy.sourceforge.net/

https://wehart.blogspot.com/2009/01/python-plugin-frameworks.html

https://docs.python.org/3/library/imp.html

https://pypi.org/project/extend_me/

https://stackoverflow.com/questions/932069/building-a-minimal-plugin-architecture-in-python