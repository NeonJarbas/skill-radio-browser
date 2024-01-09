from os.path import join, dirname

from radio_browser import RadioBrowser

from ovos_utils.ocp import MediaType, PlaybackType
from ovos_utils.parse import fuzzy_match, MatchStrategy
from ovos_workshop.decorators.ocp import ocp_search
from ovos_workshop.skills.common_play import OVOSCommonPlaybackSkill


class RadioBrowserSkill(OVOSCommonPlaybackSkill):
    def __init__(self, *args, **kwargs):
        self.supported_media = [MediaType.MUSIC,
                                MediaType.RADIO]
        self.skill_icon = join(dirname(__file__), "res", "logo.png")
        super().__init__(*args, **kwargs)

    def calc_score(self, phrase, match, idx=0, base_score=0):
        # idx represents the order from search
        score = base_score - idx  # - 1% as we go down the results list
        score += 100 * fuzzy_match(phrase.lower(), match['name'].lower(),
                                   strategy=MatchStrategy.TOKEN_SET_RATIO)
        return min(100, score)

    @ocp_search()
    def search_radio_browser(self, phrase, media_type):
        base_score = 0

        if media_type == MediaType.RADIO or self.voc_match(phrase, "radio"):
            base_score += 30

        if self.voc_match(phrase, "radio_browser"):
            base_score += 50  # explicit request
            phrase = self.remove_voc(phrase, "radio_browser")

        phrase = self.remove_voc(phrase, "radio")

        for ch in RadioBrowser.search_radio(phrase):
            score = base_score + self.calc_score(phrase, ch)
            yield {
                "match_confidence": min(100, score),
                "media_type": MediaType.RADIO,
                "uri": ch['url_resolved'],
                "playback": PlaybackType.AUDIO,
                "image": ch.get('favicon') or self.skill_icon,
                "bg_image": ch.get('favicon') or self.skill_icon,
                "skill_icon": self.skill_icon,
                "title": ch["name"],
                "length": 0
            }
