========
MicroOVN
========

.. mermaid::

   ---
   config:
     theme: default
     look: handDrawn
     layout: elk
   ---

   flowchart LR

   A(("RTD"))
   B(["OVN main"])

   A --> B

MicroOVN is a member of the Ubuntu family. It's an open source project that
warmly welcomes community projects, contributions, suggestions, fixes and
constructive feedback.

.. mermaid::

   ---
   config:
     theme: default
     layout: elk
   ---

   flowchart TD

   A(["ILB Management"])
   B["ILB"]
   C(["Backend"])

   A --> B
   B --> C

   style A fill:#FFFFFF
   style B fill:#ABB2B6
   style C fill:#FFFFFF

.. mermaid::

   ---
   config:
     theme: default
     layout: fixed
   ---

   flowchart TD

   subgraph S1["vSphere"]
          A(["ILB Management"])

     subgraph S2["ILB"]
            B["T1"]
            C["T2"]
            D["T2"]
            E["Aux"]
     end

     F(["Backend"])

   end

   A --> S2
   B --> C
   B --> D
   S2 --> F

   style A fill:#FFFFFF
   style B fill:#FFFFFF
   style C fill:#FFFFFF
   style D fill:#FFFFFF
   style E fill:#FFFFFF
   style F fill:#FFFFFF
   style S1 fill:#BBDEFB
   style S2 fill:#ABB2B6

* We follow the Ubuntu community `Code of conduct`_
* Contribute to the project on `GitHub`_ (documentation contributions go under
  the :file:`docs` directory)
* GitHub is also used as our bug tracker
* To speak with us, you can find us in our `MicroOVN Discourse`_ category.
* Optionally enable `Ubuntu Pro`_ on your OVN nodes. This is a service that
  provides the `Livepatch Service`_ and the `Expanded Security Maintenance`_
  (ESM) program.

.. toctree::
   :hidden:
   :maxdepth: 2

   how-to/index
   tutorial/index
   explanation/index
   reference/index
   developers/index

.. LINKS
.. _strictly confined snap: https://snapcraft.io/docs/snap-confinement
.. _Open Virtual Network: https://www.ovn.org/en/
.. _Code of conduct: https://ubuntu.com/community/ethos/code-of-conduct
.. _GitHub: https://github.com/canonical/microovn
.. _MicroOVN Discourse: https://discourse.ubuntu.com/c/microovn/160
.. _Ubuntu Pro: https://ubuntu.com/pro
.. _Livepatch Service: https://ubuntu.com/security/livepatch
.. _Expanded Security Maintenance: https://ubuntu.com/security/esm
