# CONTRIBUTING GUIDELINES

Ulimately {productname} is a community-driven project. Contribution is necessary, welcome, respected, and appreciated.

We do support each other to uphold our [code of conduct](CODE_OF_CONDUCT.md).

In time, efficiency wins when processing issues and pull requests. These guidelines sustain efficiency.


<!-- TOC updateonsave:true depthfrom:2 -->

- [Reporting Issues](#reporting-issues)
  - [You have a problem](#you-have-a-problem)
  - [You have a suggestion](#you-have-a-suggestion)
- [Commit Guidelines](#commit-guidelines)
  - [Format](#format)
  - [Style](#style)
- [Volunteer](#volunteer)

<!-- /TOC -->

## Reporting Issues

### You have a problem

Please be so kind as to #TODO for any open issue already covering
your problem.

----

## Commit Guidelines

Oh My Zsh uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
specification. So we are using it here. The automatic changelog tool (will soon) use these to automatically generate
a changelog based on the commit messages. Here's a guide to writing a commit message
to allow this:

### Format

```
type(scope)!: subject
```

- `type`: the type of the commit is one of the following:

  - `feat`: new features.
  - `fix`: bug fixes.
  - `docs`: documentation changes.
  - `refactor`: refactor of a particular code section without introducing
    new features or bug fixes.
  - `style`: code style improvements.
  - `perf`: performance improvements.
  - `test`: changes to the test suite.
  - `ci`: changes to the CI system.
  - `build`: changes to the build system (we don't yet have one so this shouldn't apply).
  - `chore`: for other changes that don't match previous types. This doesn't appear
    in the changelog.

- `scope`: section of the codebase that the commit makes changes to. If it makes changes to
  many sections, or if no section in particular is modified, leave blank without the parentheses.
  Examples:

  - Commit that changes the `git` plugin:
  ```
  feat(git): add alias for `git commit`
  ```

  - Commit that changes many plugins:
  ```
  style: fix inline declaration of arrays
  ```

  For changes to plugins or themes, the scope should be the plugin or theme name:

  - ✅ `fix(agnoster): commit subject`
  - ❌ `fix(theme/agnoster): commit subject`

- `!`: this goes after the `scope` (or the `type` if scope is empty), to indicate that the commit
  introduces breaking changes.

  Optionally, you can specify a message that the changelog tool will display to the user to indicate
  what's changed and what they can do to deal with it. You can use multiple lines to type this message;
  the changelog parser will keep reading until the end of the commit message or until it finds an empty
  line.

  Example (made up):

  ```
  style(agnoster)!: change dirty git repo glyph

  BREAKING CHANGE: the glyph to indicate when a git repository is dirty has
  changed from a Powerline character to a standard UTF-8 emoji. You can
  change it back by setting `ZSH_THEME_DIRTY_GLYPH`.

  Fixes #420

  Co-authored-by: Username <email>
  ```

- `subject`: a brief description of the changes. This will be displayed in the changelog. If you need
  to specify other details, you can use the commit body, but it won't be visible.

  Formatting tricks: the commit subject may contain:

  - Links to related issues or PRs by writing `#issue`. This will be highlighted by the changelog tool:
    ```
    feat(archlinux): add support for aura AUR helper (#9467)
    ```

  - Formatted inline code by using backticks: the text between backticks will also be highlighted by
    the changelog tool:
    ```
    feat(shell-proxy): enable unexported `DEFAULT_PROXY` setting (#9774)
    ```

### Style

Try to keep the first commit line short. It's harder to do using this commit style but try to be
concise, and if you need more space, you can use the commit body. Try to make sure that the commit
subject is clear and precise enough that users will know what changed by just looking at the changelog.

----

## Volunteer

#TODO  :)


## Credits

We borrowed heavily from other projects, including:
* CONTRIBUTING GUIDELINES: [@ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/blob/master/CONTRIBUTING.md)
