from jsbuilder import js


@js
def js_code():
    bleed = 100
    width = 960
    height = 760

    pack = (d3.layout.pack()
        .sort(None)
        .size([width, height + bleed * 2])
        .padding(2))

    svg = (d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(0," + (-bleed) + ")"))

    def json_read(js, error, json):
        if error:
            raise error

        node = (svg.selectAll(".node")
            .data(pack.nodes(flatten(json)))
            .filter(lambda d: not d.children)
            .enter()
                .append("g")
                .attr("class", "node")
                .attr("transform", lambda d: "translate(" + d.x + "," + d.y + ")"))

        (node.append("circle")
            .attr("r", lambda d: d.r))

        (node.append("text")
            .text(lambda d: d.name)
            .style("font-size", lambda d: Math.min(2 * d.r, (2 * d.r - 8) / getComputedTextLength() * 24) + "px")
            .attr("dy", ".35em"))

    d3.json("README.json", json_read)


print(js_code)
