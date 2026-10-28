from pathlib import Path
import stat,sys
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import configure

def test_private_configuration_roundtrip(tmp_path):
 path=tmp_path/'private/runtime.env';configure.write_env(path,{'ROCOTO_OPENAI_API_KEY':'example-private-value'})
 assert configure.read_env(path)['ROCOTO_OPENAI_API_KEY']=='example-private-value'
 assert stat.S_IMODE(path.stat().st_mode)==0o600

def test_public_and_symlink_configuration_refused(tmp_path):
 folder=tmp_path/'private';folder.mkdir(mode=0o700);path=folder/'runtime.env';path.write_text('VALUE=example\n');path.chmod(0o644)
 with pytest.raises(ValueError):configure.read_env(path)
 path.chmod(0o600);link=folder/'linked.env';link.symlink_to(path)
 with pytest.raises(ValueError):configure.read_env(link)

def test_source_checkout_configuration_refused():
 with pytest.raises(ValueError):configure.private_path(ROOT/'runtime.env')

def test_doctor_reports_names_with_values_private(tmp_path,monkeypatch,capsys):
 path=tmp_path/'private/runtime.env';configure.write_env(path,{'ROCOTO_OPENAI_API_KEY':'example-private-value'})
 monkeypatch.setattr('sys.argv',['configure.py','doctor','--features','openai','--env-file',str(path)])
 assert configure.main()==1
 output=capsys.readouterr().out;assert 'example-private-value' not in output and 'ROCOTO_PUBLIC_ORIGIN' in output
