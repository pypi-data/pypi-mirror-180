# Inkplot
Inkplot makes [PDFs](https://gitlab.com/frameworklabs/inkplot/-/raw/master/docs/examples/sample-output.pdf?inline=false)
and PNGs out of [Inkscape](https://inkscape.org/) SVG documents
using a [simple YAML file](https://gitlab.com/frameworklabs/inkplot/-/blob/master/docs/examples/render.yml)
that describes for each image or pdf page page:

* the [source SVG]()
* visibiilty for each of the SVG's layers
* the page's zoom extents

It's purpose is to make it easy to produce PDFs from SVGs where the workflow
includes turning layers on and off and zooming around to different spots
in the document space.

The project's original aim is to enable the creation of a set of planning
documents with title blocks, page numbers, compass rose and scale, etc.
with pages that include various systems like water, septic, and electrical
with labels and line weights appropriate to the scale.

I've often wanted a tool like this to exist, but only just embarked
on the project that's involved enough to justify the effort.

I hope other folks find it useful. Enjoy!

## Pages
To keep things brief, inkplot pages can use shared layersets and zoom
rectangles:
```yaml
shared:
  layersets:
    - name: hide-all
      source: farm.svg
      hidden:
        - '**'
    - name: basemap-imagery
      source: farm.svg
      visible: True
      layers:
        - "site>>basemap>>**"
    - name: titleblock-frontpage
      source: farm.svg
      visible:
        - "titleblock>>full extent frame>>boxes"
        - "titleblock>>full extent frame>>mask"
        - "scale>>full extent scale"
  zoom-rectangles:
    - name: whole-site-frame
      id: residences-site-frame-lg
    - name: both-residences-frame
      id: residences-site-frame-sm
```

To define the PDFs that can be generated using inkplot and the render definition
YAML file, A page definition can reference layersets and simply define any additional
layers that need to be turned on or off above and beyond the shared layersets
listed in `include-layersets`:
```yaml
pdfs:
  - name: example_pdf
    pages:
      - name: frontpage
        source: farm.svg
        include-layersets:
          - "hide-all"
          - "basemap-imagery"
          - "titleblock-frontpage"
        layersets:
          - visible: True
            layers:
              - "titleblock>>full extent frame>>title>>overview-basemap"
        include-zoom-rectangle: whole-site-frame
```

And, because it's a [YAML](https://yaml.org/) file, we can gain a bit more
brevity yet using YAML aliases:
```yaml
pdfs:
  - name: example_pdf
    pages:
      # this one defines the front page but also makes a template of sorts named
      # pg-imagery-with-titleblock that can be used later
      - &pg-imagery-with-titleblock
        name: frontpage
        source: farm.svg
        include-layersets:
          - "hide-all"
          - "basemap-imagery"
          - "titleblock-frontpage"
        layersets:
          - visible: True
            layers:
              - "titleblock>>full extent frame>>title>>overview-basemap"
        include-zoom-rectangle: whole-site-frame
        
      # this defines a page that includes everything in the frontpage def, but
      # redefines the layersets (keeping the layersets referenced in
      # include-layersets)
      - *pg-imagery-with-titleblock
        name: siteplan
        layersets:
            visible:
              - "titleblock>>full extent frame>>title>>site-plan"
              - "bldgs>>**"
              - "site/infrastructure/fences/**"
```

To define images, that, like pages, can be generated at the command line, we can include
an images section that is very similar to the pages section:
```yaml
images:
  - name: site-range-hill
    source: farm.svg
    include-layersets:
      - "hide-all"
      - "titleblock-brewery-site"
      - "shared-brewery-site"
    layersets:
      - visible:
          - "proposed>>brewery>>sites 1>>range hill"
      - hidden: []
    include-zoom-rectangle: brewery-site-plan-frame
```

## Using the CLI
To create all defined PDFs and images, use the simple CLI:
```bash
inkplot example.yml
```

and to create individual PDFs and images use:
```bash
# produce a single PDF
inkplot example.yml --pdf example_pdf

# produce an individual image
inkplot example.yml --image site-range-hill
```

And that should do it.

## Installing
Installing is as simple as:
```bash
pip install inkplot
```
and you'll need to have [Inkscape](https://inkscape.org) installed.
