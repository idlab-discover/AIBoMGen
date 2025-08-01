from in_toto.models.metadata import Metablock
from in_toto.models.link import Link
from securesystemslib.signer import CryptoSigner
from securesystemslib.signer._key import SSlibKey
import json
import hashlib
import os

def generate_in_toto_link(task_name, materials, products, command, signer, temp_dir, task_logger):
    """
    Generate and sign an in-toto link file for a task.

    Args:
        task_name (str): Name of the task (e.g., "run_training").
        materials (dict): Input artifacts (e.g., dataset, model, datasetdefinition).
        products (dict): Output artifacts (e.g., trained model, metrics).
        command (list): Command executed for the task.
        signer (CryptoSigner): CryptoSigner object for signing the link.
        temp_dir (str): temp_directory to save the link file.
        task_logger (logging.Logger): Logger for logging messages.
    Outputs:
        str: Path to the generated in-toto link file.
    """
    try:
        # Create the in-toto link metadata
        task_logger.info("Creating in-toto link metadata...")
        link = Link(
            name=task_name,
            materials=materials,
            products=products,
            byproducts={"stdout": "Task completed successfully."},
            command=command,
        )

        # Sign the link with the CryptoSigner
        task_logger.info("Signing in-toto link metadata...")
        link_metadata = Metablock(signed=link)
        link_metadata.create_signature(signer)

        # Save the link metadata to a temp_dir
        keyid = signer.public_key.keyid
        keyid_prefix = keyid[:8]  # Use the first 8 characters of the keyid
        link_file_path = os.path.join(temp_dir, f"{task_name}.{keyid_prefix}.link")
        task_logger.info(f"Saving in-toto link file to: {link_file_path}")
        link_metadata.dump(link_file_path)

        task_logger.info("in-toto link file generated and signed successfully.")
        return link_file_path
    except Exception as e:
        task_logger.error(f"Failed to generate in-toto link file: {str(e)}")
        raise
        
