# DiceBear Py Wrapper
[![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/dicebear) [![Downloads](https://static.pepy.tech/personalized-badge/dicebear?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/Month)](https://pepy.tech/project/dicebear) \
[`dicebear`](https://pypi.org/project/dicebear/) is an API wrapper for https://dicebear.com. Using this wrapper you can get custom avatars for your program.
\
For an example go to [`examples/dicebear.py`](https://github.com/jvherck/dicebear/tree/main/examples).

---

## Useful links
* Docs: https://jvherck.github.io/dicebear
* PyPI: https://pypi.org/project/dicebear/
* GitHub: https://github.com/jvherck/dicebear
* Dicebear: https://dicebear.com
- Dicebear CLI: https://github.com/jvherck/dicebear-cli

---

## How to install
Run `pip install dicebear`\
If that doesn't work try `py -m pip install dicebear`

---

## Usage
Important note: *Pillow* is not a required dependency, it's only required when you want to be able to edit the avatar images (using `DAvatar.pillow()`). 
When using a `PIL` function while it's not installed it will raise `dicebear.errors.PILError`.
```py
import PIL.Image
from dicebear import DAvatar, DStyle, DOptions, DColor, bulk_create


# Creating options
options = DOptions(
    backgroundColor=DColor("#00ddd0"),
    rotate=90
)


# Making a DAvatar object
av = DAvatar(
    style=DStyle.pixel_art,
    seed="John Apple",
    options=options
)
print(av.url_svg) # Prints the svg url


# Editing the DAvatar object
av.edit(
    extra_options=DOptions(backgroundColor=DColor("#000000"))
)
# Using `extra_options` keep the `rotate` option but override the `backgroundColor` option

print(av.url_png) # Prints the png url


# Editing the style specific customisations
av.customise(
    blank_options={
        "face": "variant04"
    }
)
# Using `blank_options` will delete your previous customisations for this DAvatar and generate new ones

print(av.url_png) # Prints the png url


# Converting the DAvatar object into a PIL.Image.Image object
av_img: PIL.Image.Image = av.pillow()


# Opening and viewing the DAvatar image
av.open(use_pil=True) # or av.view()


# Creating multiple random avatars of the same style at once
avatars: list = bulk_create(style=DStyle.random(), amount=10)
```

## CLI Usage
Since version 0.4.0 there's a CLI for DiceBear. It can quickly create one or more avatars at a time
but it can't take options.

__To use the CLI go to__ https://github.com/jvherck/dicebear-cli __and use `pip install dicebear-cli` to install the CLI__

---

## Customisation
Customise your avatars with these possibilities.

### Styles
All the possible avatar styles. \
https://avatars.dicebear.com/styles

* `adventurer`
* `adventurer-neutral`
* `avataaars`
* `big-ears`
* `big-ears-neutral`
* `big-smile`
* `bottts`
* `croodles`
* `croodles-neutral`
* `identicon`
* `initials`
* `micah`
* `miniavs`
* `open-peeps`
* `personas`
* `pixel-art`
* `pixel-art-neutral`

### Base Options
All the possible options for the avatar. These options work for all the styles.

* `seed` (type: `str`) - the seed for the avatar generator, determine its basic looks
* `dataUri` (type: `bool`) - whether to give the dataUri (default False)
* `flip` (type: `bool`) - flips the image vertically (default False)
* `rotate` (type: `int`) - rotates the avatar (default 0, min 0, max 360)
* `scale` (type: `int`) - the scale of the avatar drawing itself (default 100, min 0, max 200)
* `radius` (type: `int`) - the radius of the avatar (default 0, min 0, max 50)
* `size` (type: `int`) - the size of the avatar (px) (default 256, min 1, max 256)
* `backgroundColor` (type: `DColor( " #ffffff " )` ) - the background color of the avatar (default white)
* `translateX` (type: `int`) - move the avatar horizontally (default 0, min -100, max 100)
* `translateY` (type: `int`) - move the avatar vertically (default 0, min -100, max 100)

### Specific Style Options 
Specific options to get a more detailed avatar. This is different for every style. \
Click the style to see its options.

* [adventurer](https://avatars.dicebear.com/styles/adventurer#style-options)
* [adventurer-neutral](https://avatars.dicebear.com/styles/adventurer-neutral#style-options)
* [avataaars](https://avatars.dicebear.com/styles/avataaars#style-options)
* [big-ears](https://avatars.dicebear.com/styles/big-ears#style-options)
* [big-ears-neutral](https://avatars.dicebear.com/styles/big-ears-neutral#style-options)
* [big-smile](https://avatars.dicebear.com/styles/big-smile#style-options)
* [bottts](https://avatars.dicebear.com/styles/bottts#style-options)
* [croodles](https://avatars.dicebear.com/styles/croodles#style-options)
* [croodles-neutral](https://avatars.dicebear.com/styles/croodles-neutral#style-options)
* [identicon](https://avatars.dicebear.com/styles/identicon#style-options)
* [initials](https://avatars.dicebear.com/styles/initials#style-options)
* [micah](https://avatars.dicebear.com/styles/micah#style-options)
* [miniavs](https://avatars.dicebear.com/styles/miniavs#style-options)
* [open-peeps](https://avatars.dicebear.com/styles/open-peeps#style-options)
* [personas](https://avatars.dicebear.com/styles/personas#style-options)
* [pixel-art](https://avatars.dicebear.com/styles/pixel-art#style-options)
* [pixel-art-neutral](https://avatars.dicebear.com/styles/pixel-art-neutral#style-options)

### Formats 
These are the only supported formats. \
If you have Pillow (PIL) installed you can convert `DAvatar` to a `PIL.Image.Image` object to get a 
wider range of formats (Pillow doesn't support svg).

* `DFormat.png`
* `DFormat.svg`

---

## Contributing
Currently not possible yet. However you do can open an issue to report a bug
or error and I'll take a look at it.

---

## Credits
Special thanks to [DiceBear](https://github.com/dicebear) 
([Florian Körner](https://github.com/FlorianKoerner)) 
for making this amazing API and to all artists that helped 
making avatars!

## Licenses and privacy policy
- Dicebear **Licenses**: https://avatars.dicebear.com/licenses
- Dicebear **Privacy Policy**: https://avatars.dicebear.com/legal/privacy-policy
- Dicebear Python API wrapper (this project): https://github.com/jvherck/dicebear/blob/main/LICENSE