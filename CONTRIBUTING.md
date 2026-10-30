# 🤝 Contributing to Projects (`the-devod/Projects`)

Thank you for your interest in contributing to **Projects**! Our goal is to maintain clean, zero-bloat, dependency-light reference architectures across AI/voice interfaces, embedded telemetry pipelines, and developer automation utilities.

Please take a moment to review these guidelines before opening an Issue or submitting a Pull Request.

---

## 📌 Ways to Contribute

1. **Bug Reports:** Found a memory leak, serial parsing error, or broken web audio hook? Open an Issue detailing your OS, runtime version, and reproduction steps.
2. **Feature & Architecture Proposals:** Have an idea for a new modular tool or hardware mock harness? Open an Issue with the `[Proposal]` tag to discuss design before writing code.
3. **Documentation & Tutorials:** Improvements to module READMEs, wiring diagrams, type annotations, and setup guides are always welcome.
4. **Code Contributions:** Submit Pull Requests fixing open issues, adding unit tests, or decoupling modules.

---

## 🛠️ Local Development Setup

### 1. Fork and Clone
```bash
git clone [https://github.com/](https://github.com/)<your-username>/Projects.git
cd Projects
git remote add upstream [https://github.com/the-devod/Projects.git](https://github.com/the-devod/Projects.git)
```

### 2. Environment Configuration
* **Python Modules (`>= 3.10`):** Always work inside an isolated virtual environment and keep third-party dependencies to an absolute minimum.
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Windows: .venv\Scripts\activate
  ```
* **Web / Voice Interfaces:** Must remain lightweight and runnable via standard local static servers or minimal Node.js dev environments without heavy cloud lock-in.
* **C++ / Embedded Telemetry:** Ensure sketches and serial parsers compile cleanly with standard `GCC`/`Clang` or `arduino-cli` and include fallback mock data for contributors without physical sensors.

---

## 🌿 Branching & Commit Conventions

### Branch Naming
Create a descriptive branch off `main` for every change:
* `feat/<module-name>-<short-description>` (e.g., `feat/telemetry-imu-kalman-filter`)
* `fix/<module-name>-<issue>` (e.g., `fix/voice-engine-mic-timeout`)
* `docs/<short-description>` (e.g., `docs/update-quickstart-guide`)

### Conventional Commits
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification to keep history readable:
* `feat:` A new feature or module capability
* `fix:` A bug fix or edge-case patch
* `refactor:` Code restructuring without changing external behavior
* `test:` Adding or updating unit/integration tests
* `docs:` Documentation-only changes

**Example:**
```bash
git commit -m "feat(telemetry): add JSON schema validation for MPU-6050 serial stream"
```

---

## ✅ Pull Request Checklist

Before submitting your Pull Request, verify the following:

- [ ] **Zero-Bloat Principle:** No unnecessary heavy libraries or proprietary SaaS dependencies were introduced.
- [ ] **Self-Contained & Modular:** Changes are scoped cleanly to their respective module directory.
- [ ] **No Secrets or Keys:** Ensure no API keys, `.env` files, or local build artifacts are committed.
- [ ] **Tested Locally:** Code runs without warnings or unhandled exceptions on your local environment.
- [ ] **Documentation Updated:** Any new flags, endpoints, or configuration schemas are documented in the relevant `README.md`.

---

## 📜 License

By contributing to `the-devod/Projects`, you agree that your contributions will be licensed under the project's **[MIT License](LICENSE)**.
