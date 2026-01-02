# AIBoMGen Project

This repository aggregates research Proof of Concepts related to **AI Bills of Materials (AIBOMs)**.  
It contains the stable AIBoMGen v1 platform and points to ongoing work for the next generation (v2).

## AIBoMGen v1

**Release:** `v1.0-stable`  
_Branch:_ [`aibomgen-v1/main`](https://github.com/idlab-discover/AIBoMGen/tree/aibomgen-v1/main)

The original AIBoMGen platform is a proof-of-concept system that generates AIBOMs while training AI models.  
It includes:  
- **[AIBoMGen Frontend](./aibomgen-frontend/README.md)**: A Next.js-based web application for interacting with the AIBoMGen platform.
- **[AIBoMGen Platform](./aibomgen-platform/README.md)**: The backend system for distributed AI training and AIBoM generation.

Legacy branches for different experimental versions are preserved under `aibomgen-v1/...`.

## Experimental versions

### AIBoMGen v2 (Current Work)

**AIBoMGen v2** — Next-generation system for generating AIBOMs covering the **full AI lifecycle**, integrated with Kubeflow ML Metadata.  
_Branch:_ [`aibomgen-v2/main`](https://github.com/idlab-discover/AIBoMGen/tree/aibomgen-v2/main)

### AIBoMGen CRA (Moved)

The CRA-oriented AIBoMGen CLI has been moved to its own repository as it is now a separate Go module.
It is maintained independently to avoid conflicts with the Python-based v1 and v2 projects.

New repository: [AIBoMGen-cli](https://github.com/idlab-discover/AIBoMGen-cli)

## Results and Experiments

For results and experiments related to this project (v1), refer to the **[AIBoMGen Experiments repository](https://github.com/wiebe-vandendriessche/AIBoMGen-experiments)**.

## Contact

For inquiries, feel free to reach out

Maintained by:

Wiebe Vandendriessche  
[wiebe.vandendriessche@ugent.be](mailto:wiebe.vandendriessche@ugent.be)  
[LinkedIn](https://www.linkedin.com/in/wiebe-vandendriessche/?locale=en_US)  
[DISCOVER: IDLab, Ghent University – imec](https://idlab.ugent.be/research-teams/discover).

## License

This project is licensed under the terms described in the [LICENSE](./LICENSE) file.

## Acknowledgements

This work has been partially supported by the [CRACY project](https://cra-cy.eu/), funded by the European Union’s Digital Europe Programme under grant agreement No 101190492.

