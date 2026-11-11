# Robotic crack repair — paper website

Website for **Real-Time Vision-Based Adaptive Robotics for Autonomous Crack Repair in Civil Infrastructure**, Joshua Genova and Vedhus Hoskere, University of Houston. Journal of Computing in Civil Engineering (publication pending). Assigned DOI: https://doi.org/10.1061/JCCEE5.CPENG-7737.

Static HTML, CSS, and JavaScript; no build step or external runtime dependencies. Uses relative paths for GitHub Pages.

## Preview

From this directory run `python -m http.server 8000`, then open http://localhost:8000. You can also open `index.html` directly; without clipboard access the citation button selects the text for manual copying.

## Sources

- Paper details, abstract, system overview, and results follow the supplied 14-page editor proof `CP-CPENG-7737_Copy.pdf`.
- Figures are extracted directly from that proof. The full proof is not bundled; Paper links point to the author-provided [ResearchGate manuscript](https://www.researchgate.net/publication/417766419_Real-Time_Vision-Based_Adaptive_Robotics_for_Autonomous_Crack_Repair_in_Civil_Infrastructure) while publication is pending. The assigned DOI is retained in the citation metadata. Publication placeholders and editorial notes are omitted.
- The summary chart uses unweighted means of the six trial MAEs in Tables 6 and 7. Full trial values are in the paper. These experiments are separate from the paver trial in Table 8.
- The main video is the existing one-minute showcase. Footage demonstrates the apparatus and process; controller-specific numerical claims come from the paper.
- Research-code links, the resources section, and data availability are omitted until the research release is ready.

## Editing

- `index.html`: paper header, demo, abstract, system overview, experimental summary, paver testbed, and citation. The two displayed figures are the system overview and paver testbed; detailed methods and the paver convergence plot are omitted.
- `static/css/paper.css`: responsive styling.
- `static/js/paper.js`: chart metric switch and copyable citation. Update chart values and the initial HTML bar labels together if results change.
- `static/images/` and `static/videos/`: paper figures, posters, videos, and captions.
- `scripts/prepare_assets.py`: regenerate media from the proof and local video sources. Requires PyMuPDF, Pillow, and imageio-ffmpeg.

For GitHub Pages, serve the repository root from the desired branch. This work does not change repository settings or push a deployment.

## Credits and licensing

Adapted from [Nerfies](https://github.com/nerfies/nerfies.github.io), with layout inspiration from [ViewDelta](https://joshuakgao.github.io/viewdelta/). The original website template is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); retain attribution when reusing it. That template license does not apply to research media. Paper and paper figures © 2026 American Society of Civil Engineers.
