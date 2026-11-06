from flask import Flask, render_template, abort

app = Flask(__name__)

ARTICLES = [
    {"slug":"black-holes","category":"BLACK HOLES","title":"What Happens If You Fall Into a Black Hole?","subtitle":"A journey through event horizons, curved spacetime and spaghettification.","read":"8 min read","visual":"blackhole","excerpt":"What would you experience near one of the universe's most extreme objects?","sections":[
        ("A universe with an escape boundary",["A black hole is a region of spacetime bounded by an event horizon: a boundary beyond which no future-directed path can lead back to the distant universe. It is not a solid surface, and it does not act like a cosmic vacuum cleaner.","One way black holes can form is through the gravitational collapse of the core of a sufficiently massive star. The formation of supermassive black holes is more complex and remains an active area of research."]),
        ("The Schwarzschild radius",["For an idealised, non-rotating and uncharged black hole, the Schwarzschild radius is the radius of its event horizon: Rₛ = 2GM/c². Here G is the gravitational constant, M is the black-hole mass and c is the speed of light in vacuum."]),
        ("Watching from far away",["A distant observer receiving light signals from a clock falling towards a black hole would see those signals become increasingly delayed, redshifted and dimmed. The falling person's own clock, however, continues to tick normally along their path."]),
        ("Spaghettification",["The part of an object closer to a black hole is pulled more strongly than the part farther away. This difference is a tidal effect. It can stretch an object along the radial direction and compress it in other directions.","In a Newtonian approximation, the tidal acceleration difference across an object of length L is approximately Δa ≈ 2GML/r³. Tidal effects grow rapidly as distance decreases."]),
        ("Could you cross the horizon?",["For a sufficiently large black hole, a freely falling observer might cross the event horizon without noticing a dramatic local event at that exact moment. After crossing, however, all future-directed paths remain inside the horizon."]),
        ("What lies at the centre?",["In the classical, idealised Schwarzschild solution, general relativity predicts a singularity. This signals a breakdown of the classical description, not a complete physical explanation. A deeper account may require a theory combining gravity with quantum physics."])
    ],"refs":["Event Horizon Telescope Collaboration (2019), First M87 Event Horizon Telescope Results, The Astrophysical Journal Letters.","NASA, Black Holes: https://science.nasa.gov/universe/black-holes/","Einstein Online, Max Planck Institute for Gravitational Physics."]},
    {"slug":"asteroseismology","category":"STELLAR PHYSICS","title":"Asteroseismology: Listening to the Hidden Interiors of Stars","subtitle":"How tiny stellar vibrations reveal what happens deep inside a star.","read":"6 min read","visual":"star","excerpt":"Stars ring with oscillations. Their patterns reveal clues about stellar structure, age and internal conditions.","sections":[("Stars are not perfectly quiet",["Stars can oscillate in distinct patterns, much like musical instruments. These vibrations can be measured as tiny changes in brightness or surface motion."]),("Reading the patterns",["Different oscillation modes probe different regions of a star. Their frequencies depend on the star's internal structure, allowing researchers to test models of stellar evolution."])],"refs":["NASA and ESA mission resources on stellar oscillations."]},
    {"slug":"gravitational-waves","category":"COSMOLOGY","title":"Gravitational Waves: Ripples in Spacetime","subtitle":"What colliding black holes can teach us about the dynamic universe.","read":"5 min read","visual":"waves","excerpt":"Massive cosmic events can send tiny disturbances through spacetime itself.","sections":[("A prediction of general relativity",["Gravitational waves are disturbances in spacetime that propagate at the speed of light."]),("Listening to cosmic collisions",["Interferometers such as LIGO measure extraordinarily small changes in the distance between mirrors, opening a new observational window on the universe."])],"refs":["LIGO Scientific Collaboration and Virgo Collaboration educational resources."]}
]

@app.route("/")
def home():
    return render_template("index.html", articles=ARTICLES)

@app.route("/article/<slug>")
def article(slug):
    item = next((a for a in ARTICLES if a["slug"] == slug), None)
    if item is None:
        abort(404)
    return render_template("article.html", article=item)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
