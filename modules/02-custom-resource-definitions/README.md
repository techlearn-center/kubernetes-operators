# Module 02: Custom Resource Definitions (CRDs)

| | |
|---|---|
| **Time** | 3-5 hours |
| **Difficulty** | Beginner |
| **Prerequisites** | Module 01 completed |

---

## Learning Objectives

By the end of this module, you will be able to:

- Understand the core concepts of Custom Resource Definitions (CRDs)
- Set up and configure the required tools and environments
- Complete hands-on exercises that demonstrate practical skills
- Apply these skills in real-world scenarios
- Pass the module validation to prove your understanding

---

## Concepts

### What is Custom Resource Definitions (CRDs)?

Custom Resource Definitions (CRDs) is a fundamental component of Kubernetes Operators from Scratch: Zero to Hero. In production environments, this skill is used daily by engineers to build, deploy, and maintain reliable systems.

**Real-world analogy:** Think of Custom Resource Definitions (CRDs) like learning to read a map before navigating a city. Once you understand the fundamentals, you can find your way through any complex system.

### Why Does This Matter?

Companies like Google, Netflix, Amazon, and Meta rely on these practices to:
- Deploy thousands of times per day
- Maintain 99.99% uptime
- Scale to millions of users
- Recover from failures in minutes

### Key Terminology

| Term | Definition |
|---|---|
| **Core concept 1** | The foundational building block of this module |
| **Core concept 2** | How components interact and communicate |
| **Core concept 3** | The pattern used for reliability and scale |
| **Best practice** | The industry-standard approach to implementation |

---

## Hands-On Lab

### Prerequisites Check

Before starting, verify your environment:

```bash
# Check Docker is running
docker --version
docker compose version

# Check you have the project cloned
ls modules/02-custom-resource-definitions/
```

### Exercise 1: Setup and Configuration

**Goal:** Get the foundation in place for this module.

**Step 1:** Review the starter files
```bash
ls modules/02-custom-resource-definitions/lab/starter/
```

**Step 2:** Set up the required environment
```bash
# Follow the specific setup for this module
# Each command is explained below
cd modules/02-custom-resource-definitions/lab/starter/
```

**Step 3:** Verify the setup
```bash
# Run the validation to check your setup
bash modules/02-custom-resource-definitions/validation/validate.sh
```

**What you should see:** The validation script will show PASS for setup-related checks.

### Exercise 2: Core Implementation

**Goal:** Implement the main concept of this module.

Follow the detailed instructions in the starter directory. The solution directory contains the reference implementation if you get stuck.

**Key points:**
- Read each instruction carefully before executing
- Understand WHY each step is needed, not just WHAT to do
- If something fails, check the troubleshooting section below

### Exercise 3: Integration and Testing

**Goal:** Connect this module's work with the broader system.

- Verify your implementation works with previous modules
- Run all tests and validation scripts
- Document what you learned

---

## Starter Files

Check `lab/starter/` for:
- Configuration templates to fill in
- Skeleton code to complete
- Setup scripts to run

## Solution Files

If you get stuck, `lab/solution/` contains:
- Complete working configuration
- Fully implemented code
- Expected output examples

> **Important:** Try to complete the exercises yourself first! Looking at solutions too early reduces learning.

---

## Common Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Skipping prerequisites | Module exercises fail | Complete previous modules first |
| Copy-pasting without understanding | Cannot troubleshoot issues | Read explanations, not just commands |
| Not checking validation | Think you are done but are not | Run validate.sh after each exercise |
| Ignoring error messages | Problems compound | Read errors carefully, they tell you what is wrong |

---

## Self-Check Questions

Test your understanding before moving on:

1. What is the main purpose of Custom Resource Definitions (CRDs)?
2. How does this connect to the previous module?
3. What would happen in production without this?
4. Can you explain this concept to a non-technical person?
5. What are three things that could go wrong, and how would you fix them?

---

## You Know You Have Completed This Module When...

- [ ] All exercises completed
- [ ] Validation script passes: `bash modules/02-custom-resource-definitions/validation/validate.sh`
- [ ] You can explain the concepts without looking at notes
- [ ] You understand how this applies to real-world scenarios
- [ ] Self-check questions answered confidently

---

## Troubleshooting

### Common Issues

**Issue: Validation script fails**
- Re-read the exercise instructions
- Check that Docker containers are running
- Verify you are in the correct directory
- Compare your work with the solution files

**Issue: Docker container not starting**
```bash
docker compose logs <service-name>  # Check logs
docker compose down && docker compose up -d  # Restart
```

**Issue: Permission denied**
```bash
chmod +x validation/validate.sh  # Make script executable
sudo chown -R $USER .           # Fix ownership (Linux)
```

---

**Next: [Module 03 →](../03-controller-runtime-basics/)**
