class NLPInterpreter:
    def __init__(self):
        self.rules = {
            'Stop': {
                'action': 'BRAKE',
                'priority': 'HIGH',
                'rule': 'vehicle must stop completely'
            },
            'Speed Limit 10': {'action': 'SLOW', 'priority': 'MEDIUM', 'rule': 'vehicle must not exceed 10 km/h'},
            'Speed Limit 20': {'action': 'SLOW', 'priority': 'MEDIUM', 'rule': 'vehicle must not exceed 20 km/h'},
            'Speed Limit 30': {'action': 'SLOW', 'priority': 'MEDIUM', 'rule': 'vehicle must not exceed 30 km/h'},
            'Speed Limit 40': {'action': 'SLOW', 'priority': 'MEDIUM', 'rule': 'vehicle must not exceed 40 km/h'},
            'Speed Limit 50': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 50 km/h'},
            'Speed Limit 60': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 60 km/h'},
            'Speed Limit 70': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 70 km/h'},
            'Speed Limit 80': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 80 km/h'},
            'Speed Limit 90': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 90 km/h'},
            'Speed Limit 100': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 100 km/h'},
            'Speed Limit 110': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 110 km/h'},
            'Speed Limit 120': {'action': 'DRIVE', 'priority': 'LOW', 'rule': 'vehicle must not exceed 120 km/h'},
            'Green Light': {'action': 'CONTINUE', 'priority': 'MEDIUM', 'rule': 'vehicle can proceed'},
            'Red Light': {'action': 'BRAKE', 'priority': 'HIGH', 'rule': 'vehicle must stop'}
        }

    def interpret(self, sign_label):
        return self.rules.get(sign_label, {
            'sign': sign_label,
            'action': 'CONTINUE',
            'priority': 'LOW',
            'rule': 'maintain current speed'
        })

if __name__ == "__main__":
    nlp = NLPInterpreter()
    print(nlp.interpret('Stop'))
