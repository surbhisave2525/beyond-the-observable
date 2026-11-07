from flask import Flask, render_template, abort

app = Flask(__name__)

ARTICLES = [
    
{
    "slug": "black-holes",
    "category": "BLACK HOLES",
    "title": "What Happens If You Fall Into a Black Hole?",
    "subtitle": "A journey through event horizons, curved spacetime and spaghettification.",
    "read": "8 min read",
    "visual": "blackhole",
    "excerpt": "What would you experience near one of the universe's most extreme objects?",
    "sections": [
        (
            "Introduction",
            [
                "A black hole may seem to exist simply as the remains of a dead star, but in reality, it is much more than that. It is a gift to us, stretching the existing boundaries of human understanding and allowing us to explore the limits of the physics we know today. We have heard about black holes, read about them in books, and perhaps even studied them through videos and other sources.",
                "But have we ever wondered about one basic question? Well, some people certainly have, and that is exactly the question we are going to explore and understand today! Imagine you are travelling through space and suddenly come across a black hole. You become curious and start approaching it. You keep moving closer and closer until, eventually, you fall into it. What do you think might happen to you? Will you simply fall? Welcome to the mysterious world of black holes. Let's try to understand this better!",
                "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from within a certain boundary called the event horizon. But how does such an object come into existence?"
            ]
        ),
        (
            "How Is a Black Hole Formed?",
            [
                "Before understanding how a black hole is formed, let's first understand how a massive star works. During its lifetime, a star produces energy through nuclear fusion. Lighter elements fuse together to form heavier elements, releasing enormous amounts of energy.",
                "This energy produces outward pressure that balances the inward gravitational pull. This balance is known as hydrostatic equilibrium.",
                "But this balance does not last forever. Eventually, the star runs out of nuclear fuel and the balance breaks. Its core begins to collapse under its own gravitational attraction. This is called gravitational collapse.",
                "Imagine squeezing a huge object into a much smaller space. As its radius decreases while its mass remains the same, its density increases enormously. In the case of a sufficiently massive stellar core, gravity becomes so strong that no known pressure mechanism can stop the collapse. This can eventually lead to the formation of a black hole.",
                "Another interesting question is how to determine the radius associated with a black hole. For an idealised, non-rotating and uncharged black hole, this radius is called the Schwarzschild radius."
            ]
        ),
        (
            "The Schwarzschild Radius and Event Horizon",
            [
                "The Schwarzschild radius is given by:",
                "Rₛ = 2GM/c²",
                "Here, G is the universal gravitational constant, M is the mass of the black hole and c is the speed of light in vacuum.",
                "The event horizon is an imaginary boundary surrounding a black hole beyond which nothing can escape to the outside universe, not even light. It is basically a point of no return. Once you cross it, you cannot send signals back to the outside universe.",
                "The event horizon is not a physical surface. You would not encounter a solid barrier before crossing it. For a non-rotating, uncharged black hole, the event horizon lies at the Schwarzschild radius."
            ]
        ),
        (
            "What Happens When You Approach a Black Hole?",
            [
                "Imagine we hop onto a spaceship that can take us to the black hole at the centre of our galaxy, Sagittarius A*. As we travel through space, we can see different planets and stars. Now we are slowly approaching the black hole. At first, everything seems normal, but as we get closer, things start to become increasingly unusual.",
                "The gravitational influence of the black hole becomes stronger. The environment around it is very different from what we experience on Earth. But can we conclude that a black hole is a giant vacuum cleaner pulling everything inside? Not exactly. Let's understand this carefully."
            ]
        ),
        (
            "The Increasing Influence of Gravity",
            [
                "Black holes attract objects just like any other object with mass, but their extremely compact nature allows them to produce extraordinarily strong gravitational effects in their surroundings.",
                "As we get closer, the gravitational influence becomes increasingly important. For example, greater gravitational acceleration is required to remain at a fixed distance from the black hole.",
                "Even the path of light can bend due to the curvature of spacetime. This phenomenon is known as gravitational lensing."
            ]
        ),
        (
            "What Happens to Time Near a Black Hole?",
            [
                "According to Einstein, gravity affects not only space but also time. This phenomenon is called gravitational time dilation.",
                "As you approach a black hole, time passes more slowly relative to an observer who is far away from it. Your friend observing you from a safe distance would receive light signals that become increasingly delayed, redshifted and dimmed as you approach the event horizon.",
                "However, from your own perspective, your clock would continue to tick normally."
            ]
        ),
        (
            "Approaching the Event Horizon",
            [
                "As you continue travelling towards the black hole, you eventually approach its event horizon. For a sufficiently large black hole, you might cross this boundary without noticing any sudden physical change at that exact moment.",
                "But there is no turning back now. Once you cross the event horizon, all possible future paths lead you deeper into the black hole.",
                "And this brings us to an even more interesting question: what would happen to your body as you get closer to the black hole? Would you remain in one piece, or would the enormous difference in gravitational forces stretch you apart? This phenomenon is called spaghettification!"
            ]
        ),
        (
            "Spaghettification: How Does a Black Hole Stretch You Apart?",
            [
                "Imagine that you have crossed the event horizon of a black hole and are travelling further inside. As you move closer towards its centre, something strange begins to happen to your body. Your feet, being closer to the centre of the black hole than your head, experience a stronger gravitational pull.",
                "As a result, your body starts stretching in the direction of the black hole while simultaneously being compressed from the sides. Eventually, you would be stretched into a long, thin shape, almost like a strand of spaghetti!",
                "Take a simple example of the Earth and Moon. Gravitational differences across the Earth contribute to ocean tides. A similar phenomenon occurs when you approach a black hole, except the gravitational differences can become enormously large.",
                "Imagine falling feet-first into the black hole. Your feet are closer to it, so they experience a stronger pull, while your head experiences a weaker pull. These differences in gravitational acceleration stretch your body along its length. At the same time, there is sideways compression. These stretching and compression effects are known as tidal forces.",
                "According to Newton's law of universal gravitation, the gravitational force between two masses is:",
                "F = Gm₁m₂/r²",
                "Here, the gravitational force depends on the inverse square of the distance. As you get closer to the black hole, the gravitational force increases rapidly.",
                "For an object of length L falling radially towards a non-rotating black hole, the approximate difference in gravitational acceleration between its nearer and farther ends is:",
                "Δa ≈ 2GML/r³",
                "Here, L represents the length of the object, M is the black-hole mass and r is approximately the distance of its centre from the black hole. Tidal effects increase very rapidly as the distance decreases because they depend on 1/r³.",
                "Can we survive spaghettification? The answer depends on the mass of the black hole. In the case of a smaller, stellar-mass black hole, tidal forces near the event horizon can be strong enough to stretch and destroy an object even before it crosses the event horizon.",
                "However, things are different for a supermassive black hole. Because of its enormous mass, its event horizon is much farther from its centre. Consequently, tidal forces at the event horizon can be relatively weak. You could theoretically cross the event horizon of a sufficiently massive black hole without immediately experiencing spaghettification. However, as you travel deeper inside, tidal forces eventually become destructive.",
                "A fascinating fact: the term spaghettification is an actual term used in astrophysics to describe the extreme stretching of objects due to strong tidal gravitational forces. The bigger the black hole, the weaker its tidal forces can be at its event horizon."
            ]
        ),
        (
            "Can We Actually Escape a Black Hole?",
            [
                "Now that we have understood how a black hole can stretch an object apart, another interesting question arises: can you ever escape a black hole once you fall into it? Unfortunately, the answer is no!",
                "Once you cross the event horizon, escaping the black hole becomes physically impossible according to Einstein's General Theory of Relativity. But why is that so?",
                "The answer lies in the curvature of spacetime. According to Einstein's General Theory of Relativity, massive objects curve the spacetime around them. A black hole produces such extreme curvature that, inside its event horizon, all possible future paths lead towards smaller radial distances. Moving towards the outside universe is no longer a possible future direction, even for light.",
                "It is important to understand that light does not suddenly stop travelling or slow down inside a black hole. It continues travelling at the speed of light locally, but the structure of spacetime itself prevents it from escaping."
            ]
        ),
        (
            "The Singularity: What Lies at the Centre?",
            [
                "Now comes perhaps the most mysterious part of a black hole: the singularity. In the simplest mathematical description of a non-rotating black hole, the singularity lies at its centre.",
                "According to classical General Relativity, spacetime curvature becomes infinite at the singularity, and our existing theory can no longer provide a meaningful description of what happens there.",
                "What does this actually mean? It tells us that our current understanding of physics is incomplete under these extreme conditions. Physicists believe that understanding the singularity will require a theory of quantum gravity, which aims to combine General Relativity with quantum mechanics. However, we do not yet have a complete, experimentally verified theory that explains what happens at the singularity.",
                "If you continued falling inside a black hole, classical General Relativity predicts that you would eventually reach the singularity within a finite amount of your own proper time. By then, the extreme gravitational conditions would have destroyed you."
            ]
        ),
        (
            "Conclusion: The Mystery of Black Holes",
            [
                "Black holes are much more than mysterious dark objects floating in space. They are extraordinary cosmic laboratories that allow us to explore some of the most fundamental questions about our universe.",
                "From gravitational collapse and spacetime curvature to gravitational time dilation and spaghettification, black holes challenge our understanding of the laws of physics.",
                "Although Einstein's General Theory of Relativity has helped us understand many of their remarkable properties, several questions remain unanswered, particularly about what happens deep inside a black hole.",
                "Perhaps the most fascinating thing about black holes is not just what we know about them, but how much we still have to discover. After all, the universe is full of mysteries, and black holes remind us that there is still so much left to understand."
            ]
        )
    ],
    "refs": [
        "NASA – Black Holes: https://science.nasa.gov/universe/black-holes/",
        "NASA – 10 Questions You Might Have About Black Holes: https://science.nasa.gov/universe/10-questions-you-might-have-about-black-holes/",
        "Einstein Online – Relativity",
        "Event Horizon Telescope",
        "Video reference: https://youtu.be/BKIkTKqWMfg"
    ]
},

    
{
    "slug": "asteroseismology",
    "category": "STELLAR PHYSICS",
    "title": "Asteroseismology: Listening to the Hidden Interiors of Stars",
    "subtitle": "How tiny stellar vibrations reveal the secrets hidden deep within stars.",
    "read": "10 min read",
    "visual": "star",
    "excerpt": "Stars are constantly vibrating beneath their glowing surfaces. By studying these tiny oscillations, astronomers can uncover their mass, age, internal structure and evolutionary history.",
    "sections": [
        (
            "1. What Is Asteroseismology?",
            [
                "When we look at the night sky, stars appear to be silent points of light. However, beneath their glowing surfaces, stars are constantly vibrating, expanding and contracting in rhythmic patterns.",
                "Asteroseismology is the study of oscillations in stars. The term combines astero, meaning star, and seismology, the study of seismic waves and vibrations.",
                "The idea is similar to terrestrial seismology. Geologists study earthquake waves to understand Earth's internal layers, while astronomers study stellar oscillations to investigate the interiors of stars.",
                "These oscillations allow astronomers to estimate stellar mass and radius, age and evolutionary stage, internal density and temperature distribution, core structure and rotation."
            ]
        ),
        (
            "2. Why Do Stars Vibrate?",
            [
                "A star exists in a state of approximate hydrostatic equilibrium, maintained by two competing forces.",
                "Gravity pulls matter towards the centre of the star, while internal pressure generated by hot gas and radiation pushes outward, resisting gravitational collapse.",
                "Small disturbances can cause a star to oscillate around its equilibrium position. For example, when a region becomes compressed, its temperature and pressure increase. The resulting restoring force pushes the material outward and can generate waves travelling through the stellar interior.",
                "Two important categories of stellar oscillations are pressure modes and gravity modes.",
                "Pressure modes (P-modes) are acoustic waves in which pressure acts as the restoring force. They are similar to ordinary sound waves and are useful for studying the outer and intermediate regions of stars.",
                "Gravity modes (G-modes) are oscillations in which buoyancy acts as the restoring force. They are especially useful for investigating deep stellar interiors, including regions close to the core."
            ]
        ),
        (
            "3. How Do Astronomers Detect Stellar Vibrations?",
            [
                "Astronomers cannot place instruments directly on distant stars. Instead, they observe tiny variations in the light emitted by stars.",
                "As a star oscillates, its surface temperature and luminosity change slightly. Highly sensitive telescopes can measure these variations.",
                "Step 1: Measuring stellar brightness. Telescopes continuously record the brightness of a star over time. These measurements are known as light curves.",
                "Step 2: Identifying periodic variations. The brightness measurements are analysed to identify repeating patterns. Several oscillation modes can occur simultaneously, producing multiple overlapping frequencies.",
                "Step 3: Fourier analysis. Astronomers apply Fourier transforms to convert brightness variations recorded over time into a frequency spectrum.",
                "The resulting graph is called a power spectrum. It displays the frequencies at which a star oscillates and the corresponding strength of each oscillation. Each peak represents an oscillation frequency associated with a particular stellar mode.",
                "These frequencies depend on the internal structure of the star. By comparing observed patterns with theoretical stellar models, scientists can infer the physical conditions inside it.",
                "Stars do not produce sound that travels through the vacuum of space to Earth. Listening to stars is a metaphor for detecting their internal vibrations through light and surface motion."
            ]
        ),
        (
            "4. The Mathematics Behind Asteroseismology",
            [
                "Asteroseismology combines observational astronomy with mathematical physics. Two particularly important quantities are the large frequency separation and the frequency of maximum oscillation power.",
                "A. Large Frequency Separation (Δν)",
                "The large frequency separation is the difference between the frequencies of consecutive radial orders for oscillation modes having the same angular degree.",
                "Δν ≈ [2 ∫₀ᴿ (dr/cₛ)]⁻¹",
                "Here, R is the stellar radius, cₛ is the local speed of sound and dr represents a small radial distance inside the star.",
                "The large frequency separation is approximately proportional to the square root of the mean stellar density:",
                "Δν ∝ √ρ̄",
                "Stars with higher mean densities generally have larger frequency separations.",
                "B. Frequency of Maximum Power (νmax)",
                "Stellar oscillations do not all have the same amplitude. There is a particular frequency at which oscillation power reaches its maximum, represented by νmax.",
                "Its approximate scaling relation is:",
                "νmax ∝ g / √Teff",
                "Here, g is the surface gravitational acceleration and Teff is the effective temperature of the star.",
                "Since surface gravity is given by g = GM/R², we can write:",
                "νmax ∝ M / (R²√Teff)",
                "C. Stellar Mass and Radius Scaling Relations",
                "By comparing a star's oscillation properties with those of the Sun, astronomers can use the following approximate scaling relations.",
                "Radius: R/R☉ ≈ (νmax/νmax,☉)(Δν/Δν☉)⁻²(Teff/Teff,☉)¹ᐟ²",
                "Mass: M/M☉ ≈ (νmax/νmax,☉)³(Δν/Δν☉)⁻⁴(Teff/Teff,☉)³ᐟ²",
                "The subscript ☉ represents the corresponding solar value. These scaling relations are useful for studying large populations of stars. More detailed stellar modelling is required when higher precision is needed."
            ]
        ),
        (
            "5. Mixed Modes: A Window into the Stellar Core",
            [
                "One of the most fascinating discoveries in asteroseismology is the existence of mixed modes. These oscillations exhibit characteristics of both pressure modes and gravity modes.",
                "They behave like gravity modes in the deep stellar interior and like pressure modes in the outer envelope.",
                "Pure gravity modes in many solar-like stars are difficult to detect at the surface because their amplitudes become very small. Mixed modes provide a way to access information from the deep interior while remaining detectable at the surface.",
                "This is particularly useful when studying red giant stars. By analysing mixed-mode frequencies and period spacings, astronomers can investigate the rotation of stellar cores and distinguish between different evolutionary stages."
            ]
        ),
        (
            "6. How Space Telescopes Transformed Asteroseismology",
            [
                "Space-based telescopes transformed asteroseismology. From Earth, atmospheric disturbances, weather conditions and interruptions between observations make it difficult to measure extremely small brightness variations continuously.",
                "Kepler Space Telescope: Launched in 2009, NASA's Kepler Space Telescope was primarily designed to discover exoplanets. Its precise and continuous photometric observations also made it revolutionary for asteroseismology. It helped astronomers study oscillations in thousands of stars and investigate their internal structures, ages and evolutionary stages.",
                "Transiting Exoplanet Survey Satellite (TESS): Launched in 2018, TESS observes large portions of the sky. Along with its exoplanet discoveries, it provides valuable data on stellar oscillations, particularly in red giant stars.",
                "PLATO Mission: The European Space Agency's PLATO mission is designed to study terrestrial exoplanets around bright, nearby stars. Asteroseismology is a major part of its scientific programme, helping determine the masses, radii and ages of target stars and their planetary systems."
            ]
        ),
        (
            "7. What Can Asteroseismology Tell Us About Stellar Evolution?",
            [
                "Stars are born, evolve and eventually reach the end of their lives. Observing their surfaces alone does not always reveal their exact evolutionary stage. Asteroseismology provides another way to understand how stars change over time.",
                "Determining stellar age: As a star evolves, nuclear reactions gradually change its internal chemical composition. Hydrogen in the core is consumed while helium accumulates. These changes affect sound speed, density distribution and oscillation frequencies.",
                "By comparing observed oscillation frequencies with theoretical stellar evolution models, astronomers can estimate stellar ages.",
                "Understanding red giant stars: When a star like our Sun exhausts the hydrogen fuel in its core, it eventually expands into a red giant. Its internal structure becomes more complex, with a dense core surrounded by an extended envelope.",
                "Mixed-mode oscillations allow astronomers to investigate red giant interiors and distinguish between stars burning hydrogen in a shell and those burning helium in their cores.",
                "Studying internal rotation: Stars do not necessarily rotate at the same speed throughout their interiors. Their cores and outer envelopes can rotate at different rates.",
                "Rotation affects oscillation frequencies, producing a phenomenon known as rotational splitting. By examining this splitting, astronomers can investigate stellar rotation at different depths and study how angular momentum is transported within stars as they evolve."
            ]
        ),
        (
            "8. Asteroseismology and the Search for Habitable Planets",
            [
                "Asteroseismology is also important in the study of planets beyond our Solar System.",
                "When astronomers discover an exoplanet, they need to determine the properties of its host star accurately. The size of a planet is often calculated using the radius of its host star. Estimates of planetary mass and orbital characteristics also depend on accurate stellar parameters.",
                "If the properties of the host star are uncertain, the estimated properties of its planets may also be inaccurate.",
                "Asteroseismology provides independent constraints on stellar mass, radius and age, improving our understanding of exoplanetary systems.",
                "Although asteroseismology cannot directly establish whether a planet is habitable, it helps astronomers characterise the star that provides its energy."
            ]
        ),
        (
            "9. Challenges and Limitations",
            [
                "Despite its remarkable achievements, asteroseismology is not without challenges.",
                "Extremely small signals: Stellar brightness variations can be very small, requiring highly sensitive instruments.",
                "Observational limitations: Long and continuous observations are often necessary to distinguish closely spaced oscillation frequencies.",
                "Complex stellar interiors: Rotation, magnetic fields, chemical composition and convection can influence oscillation patterns.",
                "Theoretical uncertainties: Stellar models do not perfectly reproduce every observed oscillation frequency. Additional physical processes sometimes need to be incorporated into the models.",
                "Mode identification: Different oscillation modes can overlap, making their identification and interpretation difficult.",
                "Scientists continue to develop better observational techniques and more sophisticated computational models to overcome these challenges."
            ]
        ),
        (
            "10. The Future: A New Way of Understanding the Universe",
            [
                "Asteroseismology has changed the way astronomers investigate stars. Earlier, scientists mainly depended on surface observations, such as luminosity, temperature and spectral properties, to understand stellar structure.",
                "Today, stellar oscillations provide an additional and powerful source of information about stellar interiors.",
                "With continuing observations from missions such as TESS and the scientific programme of ESA's PLATO mission, astronomers hope to investigate increasingly large and diverse populations of stars.",
                "Future research may improve our understanding of the internal rotation of stars, chemical mixing inside stellar cores, the evolution of massive stars, the ages of different stellar populations in the Milky Way, and the formation and evolution of planetary systems.",
                "The more precisely we understand stars, the better we can understand the history and evolution of our galaxy."
            ]
        ),
        (
            "Conclusion: Every Star Has a Story to Tell",
            [
                "The universe may appear silent, but its stars are far from motionless. Beneath their glowing surfaces, waves travel through enormous volumes of hot plasma, carrying information about their internal structure, composition and evolution.",
                "Asteroseismology transforms these tiny stellar vibrations into valuable scientific information. By studying oscillation frequencies, astronomers can estimate the mass, radius and age of stars, investigate their cores and understand how they evolve over billions of years.",
                "Perhaps the most beautiful aspect of this field is that we do not need to travel to a star to understand its interior. We only need to observe its light carefully enough.",
                "The stars may be millions or billions of kilometres away, but their vibrations bring us closer to understanding what lies within them.",
                "Sometimes, the universe reveals its greatest secrets not through what we see, but through the subtle rhythms hidden in the light."
            ]
        ),
        (
            "About the Author",
            [
                "Surbhi Save is a physics student with an interest in astrophysics, stellar evolution and the fascinating physical processes that govern our universe. Through science writing, she aims to make complex astronomical concepts accessible and engaging for curious readers."
            ]
        )
    ],
    "refs": [
        "García, R. A., & Ballot, J. (2019). Asteroseismology of solar-type stars. Living Reviews in Solar Physics.",
        "Aerts, C. (2021). Asteroseismology Across the Hertzsprung–Russell Diagram. Annual Review of Astronomy and Astrophysics.",
        "European Space Agency (ESA). Asteroseismology – The Music of the Stars.",
        "NASA Science. Resources on stellar oscillations and the Kepler Space Telescope.",
        "Chaplin, W. J., & Miglio, A. (2013). Asteroseismology of Solar-Type and Red-Giant Stars. Annual Review of Astronomy and Astrophysics."
    ]
},

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
