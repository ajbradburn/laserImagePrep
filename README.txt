I use a sino-galvo metal etching laser to trace circuit designs onto copper plated boards.

These scripts will process SVG files that are exported by KiCad (7 and 8 are tested) in a way that converts the complicated SVG files into something that can be easily processed by LightBurn.

This is a 'simply' way of doing these conversions that isn't elegant, but works well for anything I've wanted to do.

It can also be used for converting other image types to SVG suitable for use in LightBurn, but is limited to monochome images.

To setup environment:
apt install cairosvg imagemagick 
