from obspy import read_inventory

inv = read_inventory('F1_423_small.xml')

resp = inv.networks[0].stations[0].channels[0].response

for stage in resp.response_stages:
    print(stage.stage_sequence_number, type(stage), stage.decimation_input_sample_rate, stage.decimation_factor, stage.stage_gain)
