import wget
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            local=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['local'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
