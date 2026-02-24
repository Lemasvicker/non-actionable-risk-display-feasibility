# Non-Actionable Risk Display Feasibility

Feasibility metrics, schemas, and a minimal validator for **non-actionable** risk display workflows in digital health (non-proprietary).

## What this is
This repository provides:
- A small feasibility-focused schema for logging system + workflow metrics (uptime, latency, data yield, and operator acknowledgement)
- A validator script to keep feasibility logs consistent across pilots
- A short “methods note” style document (added in v0.1.x) describing recommended metrics

## What this is not
- Not a medical device.
- Not clinical decision support.
- Not validated for any diagnostic or therapeutic use.

## Quick start (v0.1.0)
- Schema: `schema/feasibility_log.schema.json`
- Validator: `python src/validate_log.py --input demo/feasibility_log.demo.json`

## Citation
Use the GitHub “Cite this repository” feature once `CITATION.cff` is added.
After Zenodo mints the DOI for a release, cite the DOI for that version.

## Author
Victory Nlemadim

## License
Apache License 2.0
