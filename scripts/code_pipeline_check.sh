# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set +x

export FLAGS_set_to_1d=0
DEVELOP_IF="OFF"

if [[ "$DEVELOP_IF" == "OFF" ]]; then
    cd /workspace/$2/PaConvert/
    PATH=$1
    echo "Insalling develop version paddle"
    pip uninstall -y paddlepaddle
    python -m pip install --no-cache-dir paddlepaddle==0.0.0 -f https://www.paddlepaddle.org.cn/whl/linux/cpu-mkl/develop.html
    python -c "import paddle; print('paddle version information:' ,paddle.__version__); print('paddle commit information:' ,paddle.__git_commit__)"
fi

echo "start pipline testing..."
echo '*******************start generating source and wheel distribution*******************'

python setup.py sdist bdist_wheel;check_error=$?

echo '************************************************************************************'
echo "______      _____                          _   "
echo "| ___ \    / ____|                        | |  "
echo "| |_/ /_ _| |     ___  _ ____   _____ _ __| |_ "
echo "|  __/ _  | |    / _ \\| \\_ \\ \\ / / _ \\ \\__| __|"
echo "| | | (_| | |___| (_) | | | \\ V /  __/ |  | |_ "
echo "\\_|  \\__,_|\\_____\\___/|_| |_|\\_/ \\___|_|   \\__|"
echo -e '\n************************************************************************************'
if [ ${check_error} != 0 ];then
    echo "Your PR code pipeline test check failed." 
else
    echo "Your PR code pipeline test check passed."
fi
echo '************************************************************************************'

exit ${check_error}

                                             
                                             
