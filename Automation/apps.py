import subprocess


class AppManager:

    def open(self, app_name):

        try:

            subprocess.run(
                ["open", "-a", app_name],
                check=True
            )

            return True

        except subprocess.CalledProcessError:

            return False