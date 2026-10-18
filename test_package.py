import json
import math
from pathlib import Path
import unittest


class PackageTests(unittest.TestCase):
    def test_confirmed_system_and_units(self):
        data=json.loads((Path(__file__).parent/'proxima-centauri.json').read_text())
        self.assertEqual(data['id'],'proxima-centauri')
        self.assertEqual(data['format'],1)
        star,d,b=data['bodies']
        self.assertEqual([x['name'] for x in (star,d,b)],['Proxima Centauri','Proxima Centauri d','Proxima Centauri b'])
        self.assertIsNone(star['parent'])
        self.assertLess(d['orbit'],b['orbit'])
        self.assertTrue(4<d['period']<6)
        self.assertTrue(10<b['period']<12)
        for planet in (d,b):
            self.assertEqual(planet['parent'],star['name'])
            self.assertEqual(planet['rotation'],0)
            self.assertIn('estimate',planet['features'])
            self.assertIn('minimum mass',planet['features'].lower())
            self.assertIn('unknown',planet['features'])
            for key in ('mass','radius','period','orbit'):
                self.assertTrue(math.isfinite(planet[key]) and planet[key]>0)
        self.assertIn('illustrative',data['frame'])
        self.assertTrue(all(s.startswith('https://') for s in data['sources']))


if __name__=='__main__':unittest.main()
