"""
    This module will find all the namespaces
"""
import os


def get_all_namespaces(namespace_path: str):
    """
    This function returns all the namespaces list
    """
    customization_path = namespace_path
    all_namespace = os.listdir(customization_path)
    unwanted_ns = [".md"]
    filtered_namespace = [ns for ns in all_namespace if ns[-3:] not in unwanted_ns]
    return filtered_namespace


def get_all_dev_namespace(namespace_path: str):
    """
    This function will return the list of all dev namespaces
    """
    all_namespace = get_all_namespaces(namespace_path)
    dev_identifier = ["dev", "uat", "app", "apptest"]
    dev_namespace = [
        ns for ns in all_namespace if ns[-3:] in dev_identifier or ns in dev_identifier
    ]
    return dev_namespace


def get_all_prod_namespaces(namespace_path: str):
    """
    This function will return the list of prod namespaces
    """
    all_namespace = get_all_namespaces(namespace_path)
    dev_identifier = ["dev", "uat", "app", "apptest"]
    prod_namespace = [
        ns
        for ns in all_namespace
        if ns[-3:] not in dev_identifier and ns not in dev_identifier
    ]
    return prod_namespace


def get_namespace_by_argument_and_path(args, namespace_path: str):
    """
    This function will return the namespace based on the environment
    """
    if args.namespace == "all":
        if args.env == "dev":
            namespaces = get_all_dev_namespace(namespace_path)

        if args.env == "prod":
            namespaces = get_all_prod_namespaces(namespace_path)
    else:
        namespaces = [args.namespace]

    return namespaces
