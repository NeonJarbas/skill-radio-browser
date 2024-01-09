#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-radio-browser.jarbasai=skill_radio_browser:RadioBrowserSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-radio-browser',
    version='0.0.1',
    description='ovos radio browser skill plugin',
    url='https://github.com/JarbasSkills/skill-radio-browser',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_radio_browser": ""},
    package_data={'skill_radio_browser': ['locale/*', 'res/*']},
    packages=['skill_radio_browser'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a7", "radio_browser~=0.0.1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
