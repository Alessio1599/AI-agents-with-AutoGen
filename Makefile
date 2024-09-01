# Define variables
BRANCH = main
BROWSER = open  # You can specify your preferred browser here, e.g., firefox, chrome, safari
URL3 = https://chatgpt.com/  # ChatGPT website
URL4 = https://github.com/Alessio1599/Investments # GitHub repository
URL5 = https://learn.deeplearning.ai/courses/ai-agentic-design-patterns-with-autogen/lesson/2/multi-agent-conversation-and-stand-up-comedy # Course website


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

open_gpt:
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
#    make open_gpt
#
# 3. Open the GitHub repository:
#    make open_git
#
# 4. Open the course website:
#    make open_course
