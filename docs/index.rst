===================================
Isovalent Networking for Kubernetes
===================================

Cilium is an open source project that welcomes community projects,
contributions, suggestions, fixes and constructive feedback and :doc:`Reference
<reference:index>`.

.. mermaid::

   ---
   config:
     theme: default
     look: handDrawn
     layout: dagre
   ---

   flowchart TD

   A(("RTD"))
   B(["v1.14"])
   C(["v1.15"])
   D(["v1.16"])
   E(["reference"])
   F(["main"])
   G(["public"])
   H(["pristine"])

   click A "https://app.readthedocs.com/organizations/isovalent/"
   click B "https://isovalent-microovn.readthedocs-hosted.com/v1.14"
   click C "https://isovalent-microovn.readthedocs-hosted.com/v1.15"
   click D "https://isovalent-microovn.readthedocs-hosted.com/v1.16"
   click E "https://isovalent-microovn.readthedocs-hosted.com/projects/reference"
   click F "https://isovalent-microovn.readthedocs-hosted.com/latest"
   click G "https://isovalent-microovn.readthedocs-hosted.com/public"
   click H "https://isovalent-microovn.readthedocs-hosted.com/pristine"

   A --> B
   A --> C
   A --> D
   A --> E
   A --> F
   A --> G
   A --> H

   style B fill:#BBDEFB

.. toctree::

   Overview of Isovalent Cilium Enterprise <how-to/index>
   Operations guide <tutorial/index>
   Configuration guide <explanation/index>
   User guide <developers/index>
   Isovalent product security <security/index>
   Isovalent customer support <support/index>
   Reference <https://isovalent-microovn.readthedocs-hosted.com/projects/reference/>
