import os
import pypff


# Especifique o caminho para o arquivo PST que você deseja ler
pst_file_path = 'caminho/para/seu/arquivo.pst'

# Verifique se o arquivo PST existe
if not os.path.exists(pst_file_path):
    print(f"O arquivo PST '{pst_file_path}' não foi encontrado.")
else:
    # Abra o arquivo PST
    with py_pff.file() as pst:
        pst.open(pst_file_path)

        # Acesse a árvore de pastas
        root_folder = pst.get_root_folder()
        print(f"Nome da pasta raiz: {root_folder.get_display_name()}")

        # Percorra as pastas e mensagens
        def process_folder(folder, depth=0):
            print('  ' * depth + folder.get_display_name())
            for message in folder:
                print('  ' * (depth + 1) + message.get_subject())

            for subfolder in folder:
                process_folder(subfolder, depth + 1)

        process_folder(root_folder)

        # Feche o arquivo PST
        pst.close()