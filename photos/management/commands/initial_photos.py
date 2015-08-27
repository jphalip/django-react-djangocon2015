from django.core.management.base import BaseCommand

from photos.models import Photo, Favorite


# Photos referenced here are from this Instagram account: https://instagram.com/djangoreinhardt/

data = [
  {
    'url' : 'https://igcdn-photos-f-a.akamaihd.net/hphotos-ak-xaf1/t51.2885-15/e15/11117043_438671826293037_2048187522_n.jpg',
    'is_color': True,
    'is_favorite': False,
  },
  {
    'url': 'https://scontent.cdninstagram.com/hphotos-xpt1/t51.2885-15/e15/11191505_358664477662607_68372391_n.jpg',
    'is_color': False,
    'is_favorite': True,
  },
  {
    'url' : 'https://igcdn-photos-d-a.akamaihd.net/hphotos-ak-xpa1/t51.2885-15/e15/10727824_539277912878243_424619284_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-e-a.akamaihd.net/hphotos-ak-xat1/t51.2885-15/e15/11192970_1428709784098148_150538005_n.jpg',
    'is_color': False,
    'is_favorite': True,
  },
  {
    'url' : 'https://igcdn-photos-b-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11189181_1382563512072673_1677320840_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xpa1/t51.2885-15/e15/11187004_569590986511718_900392884_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11189407_386958621507230_151365168_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xtp1/t51.2885-15/e15/11142264_896289993760356_690953981_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-a-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11189967_919910261394440_1441215996_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xpa1/t51.2885-15/e15/924763_1604010016523075_1914003548_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xfp1/t51.2885-15/e15/11190810_1387671184892798_164316686_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-h-a.akamaihd.net/hphotos-ak-xaf1/t51.2885-15/e15/10326564_370639623129439_321069741_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/e15/11193015_952985584745557_290924657_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xfa1/t51.2885-15/e15/11189168_801292449949078_679762390_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xpt1/t51.2885-15/e15/11116733_1640751879493955_1620688154_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-a-a.akamaihd.net/hphotos-ak-xfp1/t51.2885-15/e15/11189293_1386492761678048_2086948741_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-f-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11137812_902762236413957_295491504_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-h-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11184675_838689589512775_220346680_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-d-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11189383_797362980340755_1389341669_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-c-a.akamaihd.net/hphotos-ak-xtp1/t51.2885-15/e15/11142951_390272364490146_896452476_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xpa1/t51.2885-15/e15/11190293_914225878641883_1760577872_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-c-a.akamaihd.net/hphotos-ak-xfa1/t51.2885-15/e15/11191060_565775786896226_1847444280_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-e-a.akamaihd.net/hphotos-ak-xta1/t51.2885-15/e15/11079022_905866496103580_1431441762_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xpa1/t51.2885-15/e15/11187047_842291922475310_384104935_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-e-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11190297_547172648753876_363559836_n.jpg',
    'is_color': False,
    'is_favorite': False,
  },
  {
    'url' : 'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/e15/11192943_806233816112920_138969009_n.jpg',
    'is_color': True,
    'is_favorite': False,
  },
  {
    'url' : 'https://igcdn-photos-b-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/e15/11189193_975175452515665_1800403273_n.jpg',
    'is_color': False,
    'is_favorite': False,
  }
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        for photo in data:
            photo_object = Photo.objects.create(
                url=photo['url'],
                is_color=photo['is_color'],
            )
            if photo.get('is_favorite'):
                Favorite.objects.create(photo=photo_object)