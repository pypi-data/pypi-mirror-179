import json
from collections import OrderedDict

from conan.api.output import Color, cli_out_write
from conan.cli.command import conan_command, conan_subcommand
from conan.cli.commands import default_json_formatter
from conan.cli.formatters.list import list_packages_html
from conans.errors import ConanException, InvalidNameException, NotFoundException
from conans.model.package_ref import PkgReference
from conans.model.recipe_ref import RecipeReference

remote_color = Color.BRIGHT_BLUE
recipe_color = Color.BRIGHT_WHITE
reference_color = Color.WHITE
error_color = Color.BRIGHT_RED
field_color = Color.BRIGHT_YELLOW
value_color = Color.CYAN


def print_list_recipes(results):
    for remote, result in results.items():
        cli_out_write(f"{remote}:", fg=remote_color)
        if result.get("error"):
            cli_out_write(f"  ERROR: {result.get('error')}", fg=error_color)
        else:
            recipes = result.get("recipes", [])
            if not recipes:
                # FIXME: this should be an error message, NOT FOUND
                cli_out_write("  There are no matching recipe references")
            else:
                current_recipe = None
                for ref in recipes:
                    if ref.name != current_recipe:
                        current_recipe = ref.name
                        cli_out_write(f"  {current_recipe}", fg=recipe_color)

                    cli_out_write(f"    {ref}", fg=reference_color)


def print_list_recipe_revisions(results):
    for remote, result in results.items():
        name = remote if remote is not None else "Local Cache"
        cli_out_write(f"{name}:", fg=remote_color)
        if result.get("error"):
            cli_out_write(f"  ERROR: {result.get('error')}", fg=error_color)
        else:
            revisions = result.get("revisions", [])
            if not revisions:
                # FIXME: this should be an error message, NOT FOUND
                cli_out_write("  There are no matching recipe references")
            else:
                for ref in revisions:
                    cli_out_write(f"  {ref.repr_humantime()}", fg=recipe_color)


def print_list_package_revisions(results):
    for remote, result in results.items():
        name = remote if remote is not None else "Local Cache"
        cli_out_write(f"{name}:", fg=remote_color)
        if result.get("error"):
            cli_out_write(f"  ERROR: {result.get('error')}", fg=error_color)
        else:
            revisions = result.get("revisions", [])
            if not revisions:
                # FIXME: this should be an error message, NOT FOUND
                cli_out_write(f"  There are no matching package references")
            else:
                for pref in revisions:
                    cli_out_write(f"  {pref.repr_humantime()}", fg=recipe_color)


def print_list_package_ids(results):
    for remote, result in results.items():
        name = remote if remote is not None else "Local Cache"
        cli_out_write(f"{name}:", fg=remote_color)
        if result.get("error"):
            cli_out_write(f"  ERROR: {result.get('error')}", fg=error_color)
        else:
            packages = result.get("packages", [])
            if not packages:
                # It is legal not to have binaries
                cli_out_write("  There are no packages")
            else:
                for pref, binary_info in packages.items():
                    cli_out_write(f"  {pref.repr_notime()}", fg=reference_color)
                    for item, contents in binary_info.items():
                        if not contents:
                            continue
                        cli_out_write(f"    {item}:", fg=field_color)
                        if not isinstance(contents, dict):
                            for c in contents:
                                cli_out_write(f"      {c}", fg=value_color)
                        else:
                            for k, v in contents.items():
                                cli_out_write(f"      {k}={v}", fg=value_color)


def _add_remotes_and_cache_options(subparser):
    subparser.add_argument("-r", "--remote", default=None, action="append",
                           help="Remote names. Accepts wildcards")
    subparser.add_argument("-c", "--cache", action='store_true', help="Search in the local cache")


def _selected_cache_remotes(conan_api, args):
    # If neither remote nor cache are defined, show results only from cache
    remotes = []
    if args.cache or not args.remote:
        remotes.append(None)
    if args.remote:
        remotes.extend(conan_api.remotes.list(args.remote))
    return remotes


@conan_subcommand(formatters={"text": print_list_recipes, "json": default_json_formatter})
def list_recipes(conan_api, parser, subparser, *args):
    """
    Search available recipes in the local cache or in the remotes
    """
    subparser.add_argument(
        "query",
        help="Search query to find package recipe reference, e.g., 'boost', 'lib*'"
    )
    _add_remotes_and_cache_options(subparser)
    args = parser.parse_args(*args)

    remotes = _selected_cache_remotes(conan_api, args)

    results = OrderedDict()
    for remote in remotes:
        name = getattr(remote, "name", "Local Cache")
        try:
            results[name] = {"recipes": conan_api.search.recipes(args.query, remote)}
        except NotFoundException:
            # TODO: Remove this try-except whenever Artifactory is returning proper messages
            results[name] = {"error": f'There are not recipes matching {args.query}'}
        except Exception as e:
            results[name] = {"error": str(e)}

    return results


@conan_subcommand(formatters={"text": print_list_recipe_revisions, "json": default_json_formatter})
def list_recipe_revisions(conan_api, parser, subparser, *args):
    """
    List all the revisions of a recipe reference.
    """
    subparser.add_argument("reference", help="Recipe reference, e.g., libyaml/0.2.5")
    _add_remotes_and_cache_options(subparser)
    args = parser.parse_args(*args)

    ref = RecipeReference.loads(args.reference)
    if ref.revision:
        raise ConanException(f"Cannot list the revisions of a specific recipe revision")

    remotes = _selected_cache_remotes(conan_api, args)

    results = OrderedDict()
    for remote in remotes:
        name = getattr(remote, "name", "Local Cache")
        try:
            results[name] = {"revisions": conan_api.list.recipe_revisions(ref, remote=remote)}
        except NotFoundException:
            # TODO: Remove this try-except whenever Artifactory is returning proper messages
            results[name] = {"error": f"Recipe not found: '{ref}'. [Remote: {remote.name}]"}
        except Exception as e:
            results[name] = {"error": str(e)}

    return results


@conan_subcommand(formatters={"text": print_list_package_revisions, "json": default_json_formatter})
def list_package_revisions(conan_api, parser, subparser, *args):
    """
    List all the revisions of a package ID reference.
    """
    subparser.add_argument("package_reference", help="Package reference, e.g., libyaml/0.2.5"
                                                     "#80b7cbe095ac7f38844b6511e69e453a:"
                                                     "ef93ea55bee154729e264db35ca6a16ecab77eb7")
    _add_remotes_and_cache_options(subparser)
    args = parser.parse_args(*args)

    try:
        pref = PkgReference.loads(args.package_reference)
    except (ConanException, InvalidNameException):
        raise ConanException(f"{args.package_reference} is not a valid package reference,"
                             f" provide a reference in the form "
                             f"name/version[@user/channel]#RECIPE_REVISION:PACKAGE_ID")
    if pref.revision:
        raise ConanException(f"Cannot list the revisions of a specific package revision")

    remotes = _selected_cache_remotes(conan_api, args)

    results = OrderedDict()
    for remote in remotes:
        name = getattr(remote, "name", "Local Cache")
        try:
            results[name] = {"revisions": conan_api.list.package_revisions(pref, remote=remote)}
        except NotFoundException:
            # TODO: Remove this try-except whenever Artifactory is returning proper messages
            results[name] = {"error": f"Recipe or package not found: '{pref}'. [Remote: {remote.name}]"}
        except Exception as e:
            results[name] = {"error": str(e)}

    return results


def _list_packages_json(results):
    for remote, d in results.items():
        d["reference"] = repr(d["reference"])
        try:
            d["packages"] = {k.repr_notime(): v for k, v in d["packages"].items()}
        except KeyError:
            pass
    myjson = json.dumps(results, indent=4)
    cli_out_write(myjson)


@conan_subcommand(formatters={"text": print_list_package_ids, "json": _list_packages_json,
                              "html": list_packages_html})
def list_packages(conan_api, parser, subparser, *args):
    """
    List all the package IDs for a given recipe revision.
    """
    subparser.add_argument(
        "reference",
        help="Recipe reference and revision, e.g., libyaml/0.2.5#latest or "
             "libyaml/0.2.5#80b7cbe095ac7f38844b6511e69e453a"
        )
    _add_remotes_and_cache_options(subparser)
    args = parser.parse_args(*args)

    try:
        ref = RecipeReference.loads(args.reference)
    except (ConanException, InvalidNameException):
        raise ConanException(f"{args.reference} is not a valid recipe reference, provide a reference"
                             f" in the form name/version[@user/channel][#RECIPE_REVISION]")

    if not ref.revision:
        raise ConanException(f"Invalid '{args.reference}' missing revision. Please specify one "
                             "revision or '#latest' one")

    remotes = _selected_cache_remotes(conan_api, args)

    results = OrderedDict()
    for remote in remotes:
        name = getattr(remote, "name", "Local Cache")
        if ref.revision == "latest":
            try:
                ref.revision = None
                ref = conan_api.list.latest_recipe_revision(ref, remote)
            except NotFoundException:
                # TODO: Remove this try-except whenever Artifactory is returning proper messages
                results[name] = {"error": f"Recipe not found: '{ref}'. [Remote: {remote.name}]"}
                continue
            except Exception as e:
                results[name] = {"error": str(e)}
                continue
            if not ref:
                results[name] = {"error": f"There are no recipes matching '{ref}'"}
                continue
        try:
            # TODO: This should error in the cache if the revision doesn't exist
            results[name] = {"packages": conan_api.list.packages_configurations(ref, remote=remote)}
        except NotFoundException:
            # TODO: Remove this try-except whenever Artifactory is returning proper messages
            results[name] = {"error": f"Recipe not found: '{ref}'. [Remote: {remote.name}]"}
        except Exception as e:
            results[name] = {"error": str(e)}
        results[name]["reference"] = ref

    return results


@conan_command(group="Consumer")
def list(conan_api, parser, *args):
    """
    List existing recipes, revisions or packages in the cache or in remotes
    """
