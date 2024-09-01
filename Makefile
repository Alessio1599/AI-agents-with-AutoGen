# Define variables
BRANCH = main
BROWSER = open  # You can specify your preferred browser here, e.g., firefox, chrome, safari
URL3 = https://chatgpt.com/  # ChatGPT website
URL4 = https://github.com/Alessio1599/AI-agents-with-AutoGen/ # GitHub repository
URL5 = https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/ # Course website
# https://microsoft.github.io/autogen/ Autogen website

# Default target
all: pull push

# Add all changes
add:
	git add .

# Commit with a message
commit: add
	git commit -m "$(m)"

# Pull the latest changes from the remote branch
pull:
	git pull origin $(BRANCH)

# Push to the main branch
push: commit
	git push origin $(BRANCH)

# Use this to quickly pull, commit, and push with a message
q:
	make m="$(m)" pull push

gpt:
	@echo "Opening website $(URL3)..."
	$(BROWSER) $(URL3)

open_git:
	@echo "Opening GitHub..."
	$(BROWSER) $(URL4)

open_course:
	@echo "Opening course website..."
	$(BROWSER) $(URL5)

# USAGE: You can now use this Makefile to quickly commit and push changes with a single command.
# 1. To commit and push with a message:
#    make q m="Your commit message"
#
# 2. Open the ChatGPT website:
#    make gpt
#
# 3. Open the GitHub repository:
#    make open_git
#
# 4. Open the course website:
#    make open_course
