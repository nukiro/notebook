# Terminal

`zsh`
`oh-my-zsh` with `plugins=(git zsh-autosuggestions zsh-syntax-highlighting)`

## Prompt

Create file `.zsh_prompt`.

```zsh
# Colors
autoload -U colors && colors
FG_RED="%{$fg[red]%}"
FG_GREEN="%{$fg[green]%}"
FG_YELLOW="%{$fg[yellow]%}"
FG_BLUE="%{$fg[blue]%}"
FG_MAGENTA="%{$fg[magenta]%}"
FG_CYAN="%{$fg[cyan]%}"
FG_WHITE="%{$fg[white]%}"
RESET="%{$reset_color%}"

# Git branch + status
git_prompt() {
  command -v git >/dev/null 2>&1 || return ""
  [[ ! -d .git && ! -d $(git rev-parse --git-dir 2>/dev/null) ]] && return ""

  local branch git_status=""

  branch=$(git symbolic-ref --quiet --short HEAD 2>/dev/null) || \
    branch=$(git rev-parse --short HEAD 2>/dev/null) || return ""

  local staged unstaged untracked

  staged=$(git diff --cached --name-only 2>/dev/null | wc -l 2>/dev/null)
  staged=${staged//[!0-9]/}; [[ -z $staged ]] && staged=0

  unstaged=$(git diff --name-only 2>/dev/null | wc -l 2>/dev/null)
  unstaged=${unstaged//[!0-9]/}; [[ -z $unstaged ]] && unstaged=0

  untracked=$(git ls-files --others --exclude-standard 2>/dev/null | wc -l 2>/dev/null)
  untracked=${untracked//[!0-9]/}; [[ -z $untracked ]] && untracked=0

  (( staged > 0 )) && git_status+=" ●${staged}"
  (( unstaged > 0 )) && git_status+=" ✚${unstaged}"
  (( untracked > 0 )) && git_status+=" ?${untracked}"

  if [[ -n $branch || -n $git_status ]]; then
    echo "on ${branch}${git_status}"
  else
    echo ""
  fi
}

# --- PROMPT ---
if [[ -n "$SSH_CONNECTION" ]]; then
  PROMPT="${FG_RED}[SSH]${RESET} ${FG_GREEN}%n${RESET}@${FG_BLUE}%m${RESET} ${FG_YELLOW}%~${RESET} ${FG_MAGENTA}\$(git_prompt)${RESET} %# "
else
  PROMPT="${FG_GREEN}%n${RESET}@${FG_BLUE}%m${RESET} ${FG_YELLOW}%~${RESET} ${FG_MAGENTA}\$(git_prompt)${RESET} %# "
fi
# --- RPROMPT: clock + error code if last command failed ---
RPROMPT='$( [[ $? -ne 0 ]] && echo "${FG_RED}✖($?) ${RESET}" )%D{%I:%M:%S %p}'
```

Import it in your `.zshrc`.

```zsh
[[ -f ~/.zsh_prompt ]] && source ~/.zsh_prompt
```
