# FUNCTIONS
annotation   = ("annotation()", "annotation(${1})")
attr         = ("attr()", "attr(${1:name})")
blur         = ("blur()", "blur(${1:<length>})")
brightness   = ("brightness()", "brightness(${1})")
calc         = ("calc()", "calc(${1})")
character_variant = ("character-variant()", "character-variant(${1})")
circle       = ("circle()", "circle(${1})")
content      = ("content()", "content(${1})")
contrast     = ("contrast()", "contrast(${1})")
counter      = ("counter()", "counter(${1:<ident>}${2:, ${3:<list-style-type>}})")
counters     = ("counters()", "counters(${1:<ident>}, \"${2:<string>}\"${3:, ${4:<list-style-type>}})")
cross_fade   = ("cross-fade()", "cross-fade(${1})")
cubic_bezier = ("cubic-bezier()", "cubic-bezier(${1:0}, ${2:0}, ${3:0}, ${4:0})")
drop_shadow  = ("drop-shadow()", "drop-shadow(${1:<length>} ${2:<length})")
element      = ("element()", "element(#${1})")
ellipse      = ("ellipse()", "ellipse(${1})")
filter_func  = ("filter()", "filter(${1})")
format_func  = ("format()", "format(\"${1}\")")
grayscale    = ("grayscale()", "grayscale(${1})")
hsl          = ("hsl()", "hsl(${1:0}, ${2:0}%, ${3:0}%)")
hsla         = ("hsla()", "hsla(${1:0}, ${2:0}%, ${3:0}%, ${4:0.0})")
hue_rotate   = ("hue-rotate()", "hue-rotate(${1:<angle>})")
icc_color    = ("icc-color()", "icc-color(${1})")
image_func   = ("image()", "image(${1})")
image_set    = ("image-set()", "image-set(${1})")
inset        = ("inset()", "inset(${1})")
invert       = ("invert()", "invert(${1})")
local        = ("local()", "local(${1})")
matrix       = ("matrix()", "matrix(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0})")
matrix3d     = ("matrix3d()", "matrix3d(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0}, ${7:0}, ${8:0}, ${9:0}, ${10:0}, ${11:0}, ${12:0}, ${13:0}, ${14:0}, ${15:0}, ${16:0})")
minmax       = ("minmax()", "minmax(${1}, ${2})")
opacity      = ("opacity()", "opacity(${1})")
ornaments    = ("ornaments()", "ornaments(${1})")
perspective  = ("perspective()", "perspective(${1:<length>})")
polygon      = ("polygon()", "polygon(${1})")
repeat       = ("repeat()", "repeat(${1})")
rgb          = ("rgb()", "rgb(${1:0}, ${2:0}, ${3:0})")
rgba         = ("rgba()", "rgba(${1:0}, ${2:0}, ${3:0}, ${4:0.0})")
rotate       = ("rotate()", "rotate(${1:<angle>})")
rotate3d     = ("rotate3d()", "rotate3d(${1:0}, ${2:0}, ${3:0}, ${4:<angle>})")
rotateX      = ("rotateX()", "rotateX(${1:<angle>})")
rotateY      = ("rotateY()", "rotateY(${1:<angle>})")
rotateZ      = ("rotateZ()", "rotateZ(${1:<angle>})")
saturate     = ("saturate()", "saturate(${1})")
scale        = ("scale()", "scale(${1:0}${2:, ${3:0}})")
scale3d      = ("scale3d()", "scale3d(${1:0}, ${2:0}, ${3:0})")
scaleX       = ("scaleX()", "scaleX(${1:0})")
scaleY       = ("scaleY()", "scaleY(${1:0})")
scaleZ       = ("scaleZ()", "scaleZ(${1:0})")
sepia        = ("sepia()", "sepia(${1})")
skew         = ("skew()", "skew(${1:<angle>}${2:, ${3:<angle>}})")
skewX        = ("skewX()", "skewX(${1:<angle>})")
skewY        = ("skewY()", "skewY(${1:<angle>})")
steps        = ("steps()", "steps(${1})")
styleset     = ("styleset()", "styleset(${1})")
stylistic    = ("stylistic()", "stylistic(${1})")
symbols      = ("symbols()", "symbols(${1})")
swash        = ("swash()", "swash(${1})")
toggle       = ("toggle()", "toggle(${1})")
translate    = ("translate()", "translate(${1:<length>}${2:, ${3:<length>}})")
translate3d  = ("translate3d()", "translate3d(${1:<length>}, ${2:<length>}, ${3:<length>})")
translateX   = ("translateX()", "translateX(${1:<length>})")
translateY   = ("translateY()", "translateY(${1:<length>})")
translateZ   = ("translateZ()", "translateX(${1:<length>})")
url          = ("url()", "url(${1})")
var          = ("var()", "var(--${1:name}, ${2:value})")
conic_gradient  = ("conic-gradient()", "conic-gradient(${1})")
linear_gradient = ("linear-gradient()", "linear-gradient(${1})")
radial_gradient = ("radial-gradient()", "radial-gradient(${1})")
repeating_conic_gradient  = ("repeating-conic-gradient()", "repeating-conic-gradient(${1})")
repeating_linear_gradient = ("repeating-linear-gradient()", "repeating-linear-gradient(${1})")
repeating_radial_gradient = ("repeating-radial-gradient()", "repeating-radial-gradient(${1})")


# TYPES
angle       = ("<angle>", "${1:<angle>}")
basic_shape = [inset, circle, ellipse, polygon]
color       = [("aliceblue",), ("antiquewhite",), ("aqua",), ("aquamarine",), ("azure",), ("beige",), ("bisque",), ("black",), ("blanchedalmond",), ("blue",), ("blueviolet",), ("brown",), ("burlywood",), ("cadetblue",), ("chartreuse",), ("chocolate",), ("coral",), ("cornflowerblue",), ("cornsilk",), ("crimson",), ("currentColor",), ("cyan",), ("darkblue",), ("darkcyan",), ("darkgoldenrod",), ("darkgray",), ("darkgreen",), ("darkgrey",), ("darkkhaki",), ("darkmagenta",), ("darkolivegreen",), ("darkorange",), ("darkorchid",), ("darkred",), ("darksalmon",), ("darkseagreen",), ("darkslateblue",), ("darkslategray",), ("darkslategrey",), ("darkturquoise",), ("darkviolet",), ("deeppink",), ("deepskyblue",), ("dimgray",), ("dimgrey",), ("dodgerblue",), ("firebrick",), ("floralwhite",), ("forestgreen",), ("fuchsia",), ("gainsboro",), ("ghostwhite",), ("gold",), ("goldenrod",), ("gray",), ("green",), ("greenyellow",), ("grey",), ("honeydew",), ("hotpink",), ("indianred",), ("indigo",), ("ivory",), ("khaki",), ("lavender",), ("lavenderblush",), ("lawngreen",), ("lemonchiffon",), ("lightblue",), ("lightcoral",), ("lightcyan",), ("lightgoldenrodyellow",), ("lightgray",), ("lightgreen",), ("lightgrey",), ("lightpink",), ("lightsalmon",), ("lightseagreen",), ("lightskyblue",), ("lightslategray",), ("lightslategrey",), ("lightsteelblue",), ("lightyellow",), ("lime",), ("limegreen",), ("linen",), ("magenta",), ("maroon",), ("mediumaquamarine",), ("mediumblue",), ("mediumorchid",), ("mediumpurple",), ("mediumseagreen",), ("mediumslateblue",), ("mediumspringgreen",), ("mediumturquoise",), ("mediumvioletred",), ("midnightblue",), ("mintcream",), ("mistyrose",), ("moccasin",), ("navajowhite",), ("navy",), ("oldlace",), ("olive",), ("olivedrab",), ("orange",), ("orangered",), ("orchid",), ("palegoldenrod",), ("palegreen",), ("paleturquoise",), ("palevioletred",), ("papayawhip",), ("peachpuff",), ("peru",), ("pink",), ("plum",), ("powderblue",), ("purple",), ("rebeccapurple",), ("red",), ("rosybrown",), ("royalblue",), ("saddlebrown",), ("salmon",), ("sandybrown",), ("seagreen",), ("seashell",), ("sienna",), ("silver",), ("skyblue",), ("slateblue",), ("slategray",), ("slategrey",), ("snow",), ("springgreen",), ("steelblue",), ("tan",), ("teal",), ("thistle",), ("tomato",), ("transparent",), ("turquoise",), ("violet",), ("wheat",), ("white",), ("whitesmoke",), ("yellow",), ("yellowgreen",), hsl, hsla, rgb, rgba]
counter_style = [("afar",), ("agaw",), ("ancient-tamil",), ("arabic-indic",), ("ari",), ("armenian",), ("bengali",), ("binary",), ("blin",), ("cambodian",), ("cambodian-consonant",), ("circle",), ("circled-decimal",), ("circled-ideograph",), ("circled-katakana",), ("circled-korean-consonant",), ("circled-korean-syllable",), ("circled-lower-latin",), ("circled-upper-latin",), ("cjk-decimal",), ("cjk-earthly-branch",), ("cjk-heavenly-stem",), ("cjk-ideographic",), ("decimal",), ("decimal-leading-zero",), ("devanagari",), ("disc",), ("disclosure-closed",), ("disclosure-open",), ("dizi",), ("dotted-decimal",), ("double-circled-decimal",), ("ethiopic-numeric",), ("filled-circled-decimal",), ("fullwidth-decimal",), ("fullwidth-lower-alpha",), ("fullwidth-lower-roman",), ("fullwidth-upper-alpha",), ("fullwidth-upper-roman",), ("gedeo",), ("georgian",), ("greek",), ("gujarati",), ("gumuz",), ("gurmukhi",), ("hadiyya",), ("harari",), ("hebrew",), ("hebrew-extended",), ("hindi",), ("hiragana",), ("hiragana-iroha",), ("japanese-formal",), ("japanese-informal",), ("kaffa",), ("kannada",), ("katakana",), ("katakana-iroha",), ("kebena",), ("kembata",), ("khmer",), ("khmer-consonant",), ("konso",), ("korean-consonant",), ("korean-hangul-formal",), ("korean-hanja-formal",), ("korean-hanja-informal",), ("korean-syllable",), ("kunama",), ("lao",), ("lepcha",), ("lower-alpha",), ("lower-alpha-symbolic",), ("lower-armenian",), ("lower-belorussian",), ("lower-bulgarian",), ("lower-greek",), ("lower-hexadecimal",), ("lower-latin",), ("lower-macedonian",), ("lower-oromo-qubee",), ("lower-roman",), ("lower-russian",), ("lower-russian-full",), ("lower-serbo-croatian",), ("lower-ukrainian",), ("lower-ukrainian-full",), ("malayalam",), ("meen",), ("mongolian",), ("myanmar",), ("new-base-60",), ("none",), ("octal",), ("oriya",), ("oromo",), ("parenthesized-decimal",), ("parenthesized-hangul-consonant",), ("parenthesized-hangul-syllable",), ("parenthesized-ideograph",), ("parenthesized-lower-latin",), ("persian",), ("persian-abjad",), ("persian-alphabetic",), ("saho",), ("shan",), ("sidama",), ("silti",), ("simp-chinese-formal",), ("simp-chinese-informal",), ("simple-lower-roman",), ("simple-upper-roman",), ("square",), ("super-decimal",), ("tamil",), ("telugu",), ("thai",), ("thai-alphabetic",), ("tibetan",), ("tigre",), ("trad-chinese-formal",), ("trad-chinese-informal",), ("upper-alpha",), ("upper-alpha-symbolic",), ("upper-armenian",), ("upper-belorussian",), ("upper-bulgarian",), ("upper-hexadecimal",), ("upper-latin",), ("upper-macedonian",), ("upper-oromo-qubee",), ("upper-roman",), ("upper-russian",), ("upper-russian-full",), ("upper-serbo-croatian",), ("upper-ukrainian",), ("upper-ukrainian-full",), ("wolaita",), ("yemsa",)]
decibel     = ("<decibel>", "${1:0}dB")
filter_func = [blur, brightness, contrast, drop_shadow, grayscale, hue_rotate, invert, opacity, saturate, sepia]
flex        = ("<flex>", "${1:0}fr")
frequency   = ("<frequency>", "${1:<frequency>}")
ident       = ("<ident>", "${1:<ident>}")
image       = [conic_gradient, cross_fade, element, filter_func, image_func, image_set, linear_gradient, radial_gradient, repeating_conic_gradient, repeating_linear_gradient, repeating_radial_gradient, url]
integer     = ("<integer>", "${1:<integer>}")
length      = ("<length>", "${1:<length>}")
number      = ("<number>", "${1:<number>}")
percentage  = ("<percentage>", "${1:0}%")
position    = [("bottom",), ("center",), ("left",), ("right",), ("top",), length, percentage, calc]
resolution  = ("<resolution>", "${1:<resolution>}")
semitones   = ("<semitones>", "${1:0}st")
string      = ("<string>", "\"${1}\"")
timing_function = [("ease",), ("ease-in",), ("ease-in-out",), ("ease-out",), ("linear",), ("step-end",), ("step-start",), cubic_bezier, steps]
time        = ("<time>", "${1:<time>}")
transform   = [matrix, matrix3d, perspective, rotate, rotate3d, rotateX, rotateY, rotateZ, scale, scale3d, scaleX, scaleY, scaleZ, skew, skewX, skewY, translate, translate3d, translateX, translateY, translateZ]
urange      = ("<urange>", "U+${1}")


# COMMON VALUES
all_values = [("inherit",), ("initial",), ("unset",), attr, toggle, var]
