import os
import subprocess
import traceback

recompile_list = [
    'block_program_zero.chinillaclvm',
    'calculate_synthetic_public_key.chinillaclvm',
    'chinillalisp_deserialisation.chinillaclvm',
    'decompress_coin_spend_entry.chinillaclvm',
    'decompress_coin_spend_entry_with_prefix.chinillaclvm',
    'decompress_puzzle.chinillaclvm',
    'delegated_tail.chinillaclvm',
    'did_innerpuz.chinillaclvm',
    'everything_with_signature.chinillaclvm',
    'genesis_by_coin_id.chinillaclvm',
    'genesis_by_puzzle_hash.chinillaclvm',
    'lock.inner.puzzle.chinillaclvm',
    'nft_metadata_updater_default.chinillaclvm',
    'nft_metadata_updater_updateable.chinillaclvm',
    'nft_ownership_layer.chinillaclvm',
    'nft_ownership_transfer_program_one_way_claim_with_royalties.chinillaclvm',
    'nft_state_layer.chinillaclvm',
    'p2_conditions.chinillaclvm',
    'p2_delegated_conditions.chinillaclvm',
    'p2_delegated_puzzle.chinillaclvm',
    'p2_delegated_puzzle_or_hidden_puzzle.chinillaclvm',
    'p2_m_of_n_delegate_direct.chinillaclvm',
    'p2_puzzle_hash.chinillaclvm',
    'p2_singleton.chinillaclvm',
    'p2_singleton_or_delayed_puzhash.chinillaclvm',
    'pool_member_innerpuz.chinillaclvm',
    'pool_waitingroom_innerpuz.chinillaclvm',
    'rom_bootstrap_generator.chinillaclvm',
    'settlement_payments.chinillaclvm',
    'sha256tree_module.chinillaclvm',
    'singleton_launcher.chinillaclvm',
    'singleton_top_layer.chinillaclvm',
    'singleton_top_layer_v1_1.chinillaclvm',
    'test_generator_deserialize.chinillaclvm',
    'test_multiple_generator_input_arguments.chinillaclvm'
]

for fname in recompile_list:
    hexfile = f'./chinilla/wallet/puzzles/{fname}.hex'
    hexdata = open(hexfile).read().strip()
    os.unlink(hexfile)
    try:
        compiled = subprocess.check_output(['../target/release/run', '-i', 'chinilla/wallet/puzzles/', f'chinilla/wallet/puzzles/{fname}']).strip()
        recompile = subprocess.check_output(['../target/release/opc', compiled]).decode('utf8').strip()
    except:
        print(f'compiling {fname}')
        traceback.print_exc()

    if hexdata != recompile:
        print(f'*** COMPILE RESULTED IN DIFFERENT OUTPUT FOR FILE {fname}')
        assert hexdata == recompile
